from __future__ import print_function
from __future__ import absolute_import
from builtins import object

import boto3
from botocore.exceptions import ClientError
from botocore.config import Config
from amicleaner.config import BOTO3_RETRIES


class OrphanSnapshotCleaner(object):

    """ Finds and removes ebs snapshots left orphaned """

    def __init__(self, ec2=None):
        self.ec2 = ec2 or boto3.client('ec2', config=Config(retries={'max_attempts': BOTO3_RETRIES}))

    def get_snapshots_filter(self):

        return [{
            'Name': 'status',
            'Values': [
                'completed',
            ]}, {
            'Name': 'description',
            'Values': [
                'Created by CreateImage*'
            ]
        }]

    def get_owner_id(self, images_json):

        """ Return AWS owner id from a ami json list """

        images = images_json or []

        if not images:
            return None

        return images[0].get("OwnerId", "")

    def fetch(self):

        """ retrieve orphan snapshots """

        resp = self.ec2.describe_images(Owners=['self'])

        used_snaps = [
            ebs.get("Ebs", {}).get("SnapshotId")
            for image in resp.get("Images")
            for ebs in image.get("BlockDeviceMappings")
        ]
        snap_filter = self.get_snapshots_filter()
        owner_id = self.get_owner_id(resp.get("Images"))

        if not owner_id:
            return []

        # all snapshots created for AMIs
        resp = self.ec2.describe_snapshots(
            Filters=snap_filter, OwnerIds=[owner_id]
        )

        all_snaps = [snap.get("SnapshotId") for snap in resp["Snapshots"]]
        return list(set(all_snaps) - set(used_snaps))

    def clean(self, snapshots):

        """
        actually deletes the snapshots with an array
        of snapshots ids
        """
        count = len(snapshots)

        snapshots = snapshots or []

        for snap in snapshots:
            try:
                self.ec2.delete_snapshot(SnapshotId=snap)
            except ClientError as e:
                self.log("{0} deletion failed : {1}".format(snap, e))
                count -= 1

        return count

    def log(self, msg):
        print(msg)
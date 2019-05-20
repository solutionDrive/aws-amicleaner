from builtins import str
from builtins import object


class AWSBlockDevice(object):
    def __init__(self):
        self.device_name = None
        self.snapshot_id = None
        self.volume_size = None
        self.volume_type = None
        self.encrypted = None

    def __str__(self):
        return str({
            'device_name': self.device_name,
            'snapshot_id': self.snapshot_id,
            'volume_size': self.volume_size,
            'volume_type': self.volume_type,
            'encrypted': self.encrypted,
        })

    @staticmethod
    def object_with_json(json):
        if json is None:
            return None

        ebs = json.get('Ebs')
        if ebs is None:
            return None

        o = AWSBlockDevice()
        o.device_name = json.get('DeviceName')
        o.snapshot_id = ebs.get('SnapshotId')
        o.volume_size = ebs.get('VolumeSize')
        o.volume_type = ebs.get('VolumeType')
        o.encrypted = ebs.get('Encrypted')

        return o

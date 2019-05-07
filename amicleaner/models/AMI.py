from builtins import str
from builtins import object
from .AWSTag import AWSTag
from .AWSBlockDevice import AWSBlockDevice


class AMI(object):
    def __init__(self):
        self.id = None
        self.architecture = None
        self.block_device_mappings = []
        self.creation_date = None
        self.hypervisor = None
        self.image_type = None
        self.location = None
        self.name = None
        self.owner_id = None
        self.public = None
        self.root_device_name = None
        self.root_device_type = None
        self.state = None
        self.tags = []
        self.virtualization_type = None

    def __str__(self):
        return str({
            'id': self.id,
            'virtualization_type': self.virtualization_type,
            'creation_date': self.creation_date,
        })

    @staticmethod
    def object_with_json(json):
        if json is None:
            return None

        o = AMI()
        o.id = json.get('ImageId')
        o.name = json.get('Name')
        o.architecture = json.get('Architecture')
        o.creation_date = json.get('CreationDate')
        o.hypervisor = json.get('Hypervisor')
        o.image_type = json.get('ImageType')
        o.location = json.get('ImageLocation')
        o.owner_id = json.get('OwnerId')
        o.public = json.get('ImageLocation')
        o.root_device_name = json.get('RootDeviceName')
        o.root_device_type = json.get('RootDeviceType')
        o.state = json.get('State')
        o.virtualization_type = json.get('VirtualizationType')

        o.tags = [AWSTag.object_with_json(tag) for tag in json.get('Tags', [])]
        ebs_snapshots = [
            AWSBlockDevice.object_with_json(block_device) for block_device
            in json.get('BlockDeviceMappings', [])
        ]
        o.block_device_mappings = [f for f in ebs_snapshots if f]

        return o

    def __repr__(self):
        return '{0}: {1} {2}'.format(self.__class__.__name__,
                                     self.id,
                                     self.creation_date)

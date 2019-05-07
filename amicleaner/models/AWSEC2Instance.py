from builtins import str
from builtins import object
from .AWSTag import AWSTag


class AWSEC2Instance(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.launch_time = None
        self.private_ip_address = None
        self.public_ip_address = None
        self.vpc_id = None
        self.image_id = None
        self.private_dns_name = None
        self.key_name = None
        self.subnet_id = None
        self.instance_type = None
        self.availability_zone = None
        self.asg_name = None
        self.tags = []

    def __str__(self):
        return str({
            'id': self.id,
            'name': self.name,
            'image_id': self.image_id,
            'launch_time': self.launch_time,
        })

    @staticmethod
    def object_with_json(json):
        if json is None:
            return None

        o = AWSEC2Instance()
        o.id = json.get('InstanceId')
        o.name = json.get('PrivateDnsName')
        o.launch_time = json.get('LaunchTime')
        o.private_ip_address = json.get('PrivateIpAddress')
        o.public_ip_address = json.get('PublicIpAddress')
        o.vpc_id = json.get('VpcId')
        o.image_id = json.get('ImageId')
        o.private_dns_name = json.get('PrivateDnsName')
        o.key_name = json.get('KeyName')
        o.subnet_id = json.get('SubnetId')
        o.instance_type = json.get('InstanceType')
        o.availability_zone = json.get('Placement').get('AvailabilityZone')
        o.tags = [AWSTag.object_with_json(tag) for tag in json.get('Tags', [])]

        return o


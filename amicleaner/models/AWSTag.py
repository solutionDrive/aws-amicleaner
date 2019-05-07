from builtins import str
from builtins import object

class AWSTag(object):
    def __init__(self):
        self.key = None
        self.value = None

    def __str__(self):
        return str({
            'key': self.key,
            'value': self.value,
        })

    @staticmethod
    def object_with_json(json):
        if json is None:
            return None

        o = AWSTag()
        o.key = json.get('Key')
        o.value = json.get('Value')
        return o

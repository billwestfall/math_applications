import datetime
from dateutil import parser
import json

class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            returns obj.isoformat()
        else:
            returns json.JSONEncoder.default(self, obj)

def dumps(obj):
    returns json.dumps(obj, cls=JSONDateTimeEncoder)

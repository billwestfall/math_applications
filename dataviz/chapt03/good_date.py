import datetime
from dateutil import parser
import json

class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            a = obj.isoformat()
        print(a)
        else:
            b = json.JSONEncoder.default(self, obj)
        print(b)

def dumps(obj):
    c = json.dumps(obj, cls=JSONDateTimeEncoder)
print(c)

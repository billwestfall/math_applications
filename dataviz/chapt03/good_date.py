import datetime
from dateutil import parser
import json

class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            a = return obj.isoformat()
        print(a)
        else:
            b = return json.JSONEncoder.default(self, obj)
        print(b)

def dumps(obj):
    c = return json.dumps(obj, cls=JSONDateTimeEncoder)
print(c)

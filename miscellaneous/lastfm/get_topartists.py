import requests
import json

headers = {
    'user-agent': "cmd_api"
}

payload = {
    'api_key': '<key>',
    'method': 'user.gettopartists',
    'period': '7day',
    'format': 'json',
    'user': '<name>',
    'limit': '5'
}

r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
status = r.status_code
y = (r.json())
#print(y)
print(y["topartists"]["artist"][0]["name"])
print(y["topartists"]["artist"][1]["name"])
print(y["topartists"]["artist"][2]["name"])
print(y["topartists"]["artist"][3]["name"])
print(y["topartists"]["artist"][4]["name"])

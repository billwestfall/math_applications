import requests
import json

headers = {
    'user-agent': "cmd_api"
}

payload = {
    'api_key': '<key>',
    'method': 'user.getrecenttracks',
    'format': 'json',
    'user': '<name>',
    'limit': '1'
}

r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
status = r.status_code
y = (r.json())
print(y["recenttracks"]["track"][0]["artist"]['#text'])
print(y["recenttracks"]["track"][0]["name"])

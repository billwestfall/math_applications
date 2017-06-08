import requests

response = requests.get("http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key=<APIKEY>&format=json")

data = response.json()
print(data.keys)

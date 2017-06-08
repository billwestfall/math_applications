import requests

response = requests.get('http://restcountries.eu/rest/v2/all')

print(response.json)

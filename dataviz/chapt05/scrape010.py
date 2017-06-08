import requests

response = requests.get('https://restcountries.eu/rest/v2/all?fields=name;capital;currencies')

print(response)

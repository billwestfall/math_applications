import requests

response = requests.get('https://restcountries.eu/rest/v2/all?fields=name;currencies')

print(response.text)

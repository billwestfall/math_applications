import requests

REST_EU_ROOT_URL = 'http://restcountries.eu/rest/v2/all'
url = 'http://restcountries.eu/rest/v2/all'

response = requests.get(url)

return response

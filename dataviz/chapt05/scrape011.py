
import requests
from pymongo import MongoClient

REST_EU_ROOT_URL = 'http://restcountries.eu/rest/v2/all'
url = 'http://restcountries.eu/rest/v2/all'
db_nobel = get_mongo_database('nobel_prize')
col = db_nobel['country_data']

response = requests.get(url)

client = MongoClient()
col.insert(country_data)


import requests
from pymongo import MongoClient

def get_mongo_database(db_name, host='localhost', port=27017, username=None, password=None):
    mongo_uri = 'mongodb://localhost:27017'
    conn = MongoClient(mongo_uri)
    
def initialize(self):
        client = pymongo.MongoClient(self.URI)
        self.DATABASE = client['nobel_prize']

REST_EU_ROOT_URL = 'http://restcountries.eu/rest/v2/all'
url = 'http://restcountries.eu/rest/v2/all'
db_nobel = get_mongo_database('nobel_prize')
col = db_nobel['country_data']

response = requests.get(url)

col.insert(country_data)


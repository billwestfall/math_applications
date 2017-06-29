import pandas as pd
from pymongo import MongoClient

df = pd.read_json(open("data/nobel_winners_dirty.json"))

def get_mongo_database(db_name, collection, query={}, host='localhost', port="27017", username="", password="", no_id="true"):
    conn = MongoClient(host, port)

def mongo_to_dataframe(db_name, collection, query={}, host='localhost', port="27017", username="", password="", no_id="true"):
    db = get_mongo_database(db_name, host, port, username, password)
    cursor = db[collection].find(query)
    df = pd.dataframe(list(cursor))

    if no_id:
        del df['_id']

    return df

df = mongo_to_dataframe('nobel_prize', 'winners')
print(df)

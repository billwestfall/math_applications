import pandas as pd
from pymongo import MongoClient

df = pd.read_json(open("data/nobel_winners_dirty.json"))

print(df)

#def get_mongo_database(db_name="nobel_prize", collection="winners", query={}, host='localhost', port=27017, username="", password="", no_id="true"):
#    conn = MongoClient()

#def mongo_to_dataframe(db_name="nobel_prize", collection="winners", query={}, host='localhost', port=27017, username="", password="", no_id="true"):
#    db = get_mongo_database(db_name, collection)
#    cursor = db[collection].find(query)
#    df = pd.dataframe(list(cursor))

#    if no_id:
#        del df['_id']
#
#    return df

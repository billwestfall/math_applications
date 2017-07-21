import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import seaborn as sb
import pymongo
from pymongo import MongoClient

def get_mongo_database(db_name="nobel_prize", collection="winners", query={}, host='localhost', port=27017, username="", password="", no_id="true"):
    conn = MongoClient()

def mongo_to_dataframe(db_name="nobel_prize", collection="winners", query={}, host='localhost', port=27017, username="", password="", no_id="true"):
    db = get_mongo_database(db_name, collection)
    cursor = db[collection].find(query)
    df = pd.dataframe(list(cursor))

    if no_id:
        del df['_id']

    return df

plt.rcParams['figure.figsize'] = 8, 4

df = mongo_to_dataframe('nobel_prize', 'winners_clean')
df.info()

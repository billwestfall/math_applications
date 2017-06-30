import pandas as pd
from pymongo import MongoClient

df = pd.read_json(open("data/nobel_winners_dirty.json"))

print(df)
print(df.info())
print(df.describe())

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

#import csv
#import json
#import pandas as pd
#import sys, getopt, pprint
#from pymongo import MongoClient
#CSV to JSON Conversion
#csvfile = open('C://test//final-current.csv', 'r')
#reader = csv.DictReader( csvfile )
#mongo_client=MongoClient() 
#db=mongo_client.october_mug_talk
#db.segment.drop()
#header= [ "S No", "Instrument Name", "Buy Price", "Buy Quantity", "Sell Price", "Sell Quantity", "Last Traded Price", "Total Traded Quantity", "Average Traded Price", "Open Price", "High Price", "Low Price", "Close Price", "V" ,"Time"]

#for each in reader:
#    row={}
#    for field in header:
#        row[field]=each[field]

#    db.segment.insert(row)

import pandas as pd
from pymongo import MongoClient

df = pd.read_json(open("data/nobel_winners_dirty.json"))

print(df.columns)
print(df.set_index('name'))
print("Set index on name")
print(df.head(2))
print(df.reset_index(inplace=True))
print("Reset index")
print(df.head(2))

import pandas as pd
from pymongo import MongoClient

df = pd.read_json(open("data/nobel_winners_dirty.json"))

print("First 10 rows")
print(df[0:10])
print("Last 4 rows")
print(df[-4:])
print("Winners after year 2000")
mask = df.year > 2000
print(mask)
winners_since_2000 = df[mask]
print("Count of winners since 2000")
print(winners_since_2000.count())
print("Head of winners since 2000")
print(winners_since_2000.head())

import pandas as pd
from pymongo import MongoClient

df = pd.read_json(open("data/nobel_winners_dirty.json"))

print("Describe born in column")
print(df.born_in.describe())
print("Setting born in to unicode")
set(df.born_in.apply(type))
print(set(df.born_in.apply(type)))

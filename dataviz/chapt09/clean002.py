import pandas as pd
from pymongo import MongoClient

df = pd.read_json(open("data/nobel_winners_dirty.json"))

print(df.columns)

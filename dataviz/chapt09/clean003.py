import pandas as pd
from pymongo import MongoClient

df = pd.read_json(open("data/nobel_winners_dirty.json"))

bi_col = df['born_in']
print("Info on born in column")
print(bi_col)
print(type(bi_col))
print("First row")
print(df.iloc[0])
print("Set index to name and locate entry by name")
df.set_index('name', inplace=True)
print(df.loc['Albert Einstein'])

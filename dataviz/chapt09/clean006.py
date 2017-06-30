import pandas as pd
import numpy as np
from pymongo import MongoClient

df = pd.read_json(open("data/nobel_winners_dirty.json"))

bi_col = df['born_in']
print("Describe born in column")
print(df.born_in.describe())
print("Setting born in to unicode")
set(df.born_in.apply(type))
print(set(df.born_in.apply(type)))
bi_col.replace('', np.nan, inplace=True)
print("Replace missing values with NaN")
print(bi_col)
print(bi_col.count())
print("Replace names with asterisk with emptry string")
df.name = df.name.str.replace('*', '')
df.name = df.name.str.strip()
print(df.name)
print("verify no asterisks")
print(df[df.name.str.contains('\*')])

print("find number of null entries")
df = df[df.born_in.isnull()]
print(df.count())

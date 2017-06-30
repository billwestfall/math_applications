import pandas as pd
import numpy as np
from pymongo import MongoClient

df = pd.read_json(open("data/nobel_winners_dirty.json"))

all_dupes = df[df.duplicated('name') | df.duplicated('name', keep='last')]
print("all duplicate entries sorted by name")
print(all_dupes.sort_values('name') [['name', 'country', 'year']])

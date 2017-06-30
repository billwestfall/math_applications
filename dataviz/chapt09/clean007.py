import pandas as pd
import numpy as np
from pymongo import MongoClient

df2 = pd.DataFrame({'name':['zak', 'alice', 'bob', 'mike', 'bob', 'bob'], 'score':[4, 3, 5, 2, 3, 7]})

frame_sort = df2.sort_values(['name', 'score'], ascending=[1,0])

print("sort on dataframe name and score values")
print(frame_sort)

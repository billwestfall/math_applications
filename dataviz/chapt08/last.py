import datetime
import pandas as pd
import numpy as np

df = pd.read_json('last.json')
#print(df)
print(df.columns)
print(df['weeklytrackchart'])
print(df.index)
df = df.set_index('track')
#print(df)
print(df.loc("name":'Begin (feat. Wales)'))
df = df.reset_index()
#print(df)

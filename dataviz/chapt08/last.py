import datetime
import pandas as pd
import numpy as np

df = pd.read_json('last.json')
#print(df)
print(df.columns)
print(df['weeklytrackchart'])
print(df.index)
df = df.set_index('weeklytrackchart')
print(df)
#print(df.loc('Psychorama'))
df = df.reset_index()
print(df)
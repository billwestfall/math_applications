import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import seaborn as sb

def mongo_to_dataframe(db_name, collection, query={}, host='localhost', port=27017):
  db = 

plt.rcParams['figure.figsize'] = 8, 4

df = mongo_to_dataframe('nobel_prize', 'winners_clean')
df.info()

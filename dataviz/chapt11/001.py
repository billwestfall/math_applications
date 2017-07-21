import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import seaborn as sb

plt.rcParams['figure.figsize'] = 8, 4

df = mongo_to_dataframe('nobel_prize', 'winners_clean')
df.info()

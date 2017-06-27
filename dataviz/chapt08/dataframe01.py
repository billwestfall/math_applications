import datetime
import pandas as pd
import numpy as np

todays_date = datetime.datetime.now().date()
index = pd.date_range(todays_date-datetime.timedelta(10), periods=10, freq='D')
data = np.array([np.arange(10)]*3).T
columns = ['A','B', 'C']

df = pd.DataFrame(data, index=index, columns=columns)
print(df)

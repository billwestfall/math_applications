import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

x = pd.period_range(pd.datetime.now(), periods=200, freq='d')
x = x.to_timestamp().to_pydatetime()
y = np.random.randn(200, 3).cumsum(0)
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.color'] = 'r'

plt.plot(x, y)
plt.show()

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

x = pd.period_range(pd.datetime.now(), periods=200, freq='d')
x = x.to_timestamp().to_pydatetime()
y = np.random.randn(200, 3).cumsum(0)

figure, ax = plt.subplots()
plots = ax.plot(x, y, label='')
figure.set)size_inches(8, 4)
ax.legend(plots, ('foo', 'bar', 'baz'), loc='best', framealpha=0.25, prop={'size':'small', 'family':'monospace'})
ax.set_title('Random trends')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative sum')
ax.grid(True)
figure.text(0.995, 0.01, u'\u00a9 Acme Designs 2015', ha='right', va='bottom')
figure.tight_layout()
figure.show()

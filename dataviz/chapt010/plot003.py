import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

x = pd.period_range(pd.datetime.now(), periods=200, freq='d')
x = x.to_timestamp().to_pydatetime()
y = np.random.randn(200, 3).cumsum(0)

plots = plt.plot(x, y)
plt.legend(plots, ('foo', 'bar', 'baz'), loc = 'best', framealpha=0.25, prop={'size':'small', 'family':'monospace'})
plt.gcf().set_size_inches(10, 6)
plt.gcf().set_tight_layout(True)
plt.title('Random trends')
plt.xlabel('Date')
plt.ylabel('Cumulative sum')
plt.grid(True)
plt.figtext(0.995, 0.01, u'\u00a9 Acme Designs 2015', ha='right', va='bottom')
#plt.tight_layout()
plt.show()

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

num_points = 100
gradient = 0.5
x = np.array(range(num_points))
y = np.random.randn(num_points) * 10 + x*gradient
data = pd.DataFrame({'dummy x':x, 'dummy y' :y})
sns.lmplot('dummy x', 'dummy y', data, size=4, aspect=2)

plt.suptitle('Scatterplot with Seaborn')
plt.savefig('mpl_scatter_seaborn.png', dpi=200)

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

num_points = 100
gradient = 0.5
x = np.array(range(num_points))
y = np.random.randn(num_points) * 10 + x*gradient
fig, ax = plt.subplots(figsize=(8, 4))
colors = np.random.rand(num_points)
size = (2 + np.random.rand(num_points) * 8) ** 2
ax.scatter(x, y, s=size, c=colors, alpha=0.5)
m, c = np.polyfit(x, y, 1)
ax.plot(x, m*x + c)

fig.suptitle('Scatterplot with regression line')
fig.savefig('mpl_regression_scatter.png', dpi=200)

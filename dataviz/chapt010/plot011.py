import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

num_points = 100
gradient = 0.5
x = np.array(range(num_points))
y = np.random.randn(num_points) * 10 + x*gradient
fig, ax = plt.subplots(figsize=(8, 4))
ax.scatter(x, y)

fig.suptitle('A Simple Scatterplot')
fig.savefig('mpl_simpl_scatter.png', dpi=200)

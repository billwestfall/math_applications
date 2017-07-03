import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

labels = ["Physics", "Chemistry", "Literature", "Peace"]
foo_data = [3, 6, 10, 4]
bar_data = [8, 3, 6, 1]

fig, ax = plt.subplots(figsize=(8, 4))
width = 0.4
ylocs = np.arange(len(foo_data))
ax.barh(ylocs-width, foo_data, width, color='#fde0bc', label='Fooland')
ax.barh(ylocs, bar_data, width, color='peru', label='Barland')
ax.set_xticks(range(12))
ax.set_yticks(ticks=range(len(foo_data)))
ax.set_yticklabels(labels)
ax.xaxis.grid(True)
ax.legend(loc='best')
ax.set_xlabel('Number of prizes')
fig.suptitle('Prizes by country')
fig.tight_layout(pad=2)
fig.savefig('mpl_barchart_horiz.png', dpi=200)

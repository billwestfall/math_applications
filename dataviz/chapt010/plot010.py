import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

labels = ["Physics", "Chemistry", "Literature", "Peace"]
foo_data = [3, 6, 10, 4]
bar_data = [8, 3, 6, 1]

fig, ax = plt.subplots(figsize=(8, 4))
bar_width = 0.8
xlocs = np.arange(len(foo_data))
ax.bar(xlocs-width, foo_data, bar_width, color='#fde0bc', label='Fooland')
ax.bar(xlocs, bar_data, bar_width, color='peru', label='Barland', bottom=foo_data)
ax.set_yticks(range(18))
ax.set_xticks(ticks=np.array(range(len(foo_data))) + bar_width/2)
ax.set_xticklabels(labels)
ax.set_xlim(-(1-bar_width), xlocs[-1]+1 )
ax.legend(loc='best')
ax.set_xlabel('Number of prizes')
fig.suptitle('Prizes by country')
fig.tight_layout(pad=2)
fig.savefig('mpl_barchart_stack.png', dpi=200)

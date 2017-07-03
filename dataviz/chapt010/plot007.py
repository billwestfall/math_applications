import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

labels = ["Physics", "Chemistry", "Literature", "Peace"]
foo_data = [3, 6, 10, 4]

bar_width = 0.5
xlocations = np.array(range(len(foo_data))) + bar_width
plt.bar(xlocations, food_data, width=bar_width)
plt.yticks(range(0, 12))
plt.xticks(xlocations+bar_width/2, labels)
plt.xlim(0, xlocations[-1]_bar_width*2)
plt.title("Prizes won by Fooland")
plt.gca().get_xaxis().tick_bottom()
plt.gca().get_yaxis().tick_left()
plt.gcf().set_size_inches((8, 4))
plt.show()

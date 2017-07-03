import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips)

pal = dict(Female='red', Male='blue')
g = sns.FacetGrid(tips, col="smoker", hue="sex", hue_kws={"marker": ["D", "s"]}, palette=pal, size=4, aspect=1)
g.map(plt.scatter, "total_bill", "tip", alpha=.4)
g.add_legend()
plt.savefig('sns_tip_scatter02.png', dpi=200)

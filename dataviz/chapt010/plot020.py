import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips)

pal = dict(Female='red', Male='blue
sns.lmplot(x="total_bill", y="tip", hue="sex", markers=["D", "s"], col="smoker", rwo="time", data=tips, palette=pal, size=4, aspect=1)

plt.savefig('sns_tip_scatter03.png', dpi=200)

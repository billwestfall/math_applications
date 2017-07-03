import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips)

g = sns.FacetGrid(tips, col="smoker")
g.map(plt.scatter, "total_bill", "tip")
plt.savefig('sns_tip_scatter01.png', dpi=200)

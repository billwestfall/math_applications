import matplotlib.pyplot as plt
import numpy as np

#fig = plt.figure() # manually create a figure
#lines = plt.plot(x, y) # plot data

x = np.linspace(-0.5, 3.0)
lines = plt.plot(x, f(x), x, x**2, x, 1 - x)

lines.show()

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
l1 = ax.plot(x, f(x))
l2 = ax.plot(x, x**2)
l3 = ax.plot(x, 1 - x)

y1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y2 = np.array([1.2, 1.6, 3.1, 4.2, 4.8])
y3 = np.array([3.2, 1.1, 2.0, 4.9, 2.5])

lines = ax.plot(y1, 'o', y2, 'x', y3, '*')

def f(x):
  return x*(x - 2)*np.exp(3 - x)
  
x = np.linspace(-0.5, 3.0)

plt.plot(x, f(x), x, x**2, x, 1 - x)
plt.show()

import numpy as np

def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s' %(a.ndim, a.shape, a.dtype))

pi = np.pi
a = np.array([pi, pi/2, pi/4, pi/6])
print("some division on pi")
print(a)
print("radians to degrees")
print(np.degrees(a))
print("sin of array")
sin_a = np.sin(a)
print(sin_a)
print("rounding on array")
print(np.round(sin_a, 7))
print("arange and reshape")
a = np.arange(8).reshape((2.4))
print(a)
print("cumulative sum")
print(np.cumsum(a, axis=1))
print("cumulative sum without specifying axis")
print(np.cumsum(a))

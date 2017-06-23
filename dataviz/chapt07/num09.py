import numpy as np

def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s' %(a.ndim, a.shape, a.dtype))

a = np.array([1, 2, 3, 4, 5, 6])
print("the array")
print(a)
a = a.reshape([2, 3])
print("reshape")
print(a)
print("some array math")
print("multiply by 2")
a = a * 2
print(a)
print("subtract 2")
a = a - 2
print(a)
print("divide by 2")
a = a / 2.0
print(a)

import numpy as np

def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s' %(a.ndim, a.shape, a.dtype))

a = np.array([1, 2, 3, 4, 5, 6])
print("element 2 in array")
print(a[2])
print("elements 3 to 5 noninclusive")
print(a[3:5])
print("insert zeros")
b = ((a[:4:2]) = 0)
print(b)
print("reversed")
print(a[::-1])

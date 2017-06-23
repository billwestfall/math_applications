import numpy as np

def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s' %(a.ndim, a.shape, a.dtype))

a = np.array([45, 65, 76, 32, 99, 22])
print("the array")
print(a)
print("boolean less than 50 test")
print(a < 50)

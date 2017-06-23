import numpy as np

def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s' %(a.ndim, a.shape, a.dtype))

a = np.zeros([2, 3])
print("create an array from a function")
print(a)
print("the data type is")
print(a.dtype)
print("create an array of ones from a function")
a = np.ones([2, 3])
print(a)

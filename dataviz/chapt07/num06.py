import numpy as np

def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s' %(a.ndim, a.shape, a.dtype))

empty_array = np.empty((2,3))

print("create an empty array")
print(empty_array)
print("create an array with random values")

rand_array = np.random.random((2,3))
print(rand_array)

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(a)

def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s' %(a.ndim, a.shape, a.dtype))

print_array_details(a)

import numpy as np

def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s' %(a.ndim, a.shape, a.dtype))

a = np.arange(8).reshape((2,4))
print("the array")
print(a)
print("the min values")
print(a.min(axis=1))
print("the sum across axes")
print(a.sum(axis=0))
print("the mean for each axes")
print(a.mean(axis=1))
print("standard deviation of each axis")
print(a.std(axis=1))

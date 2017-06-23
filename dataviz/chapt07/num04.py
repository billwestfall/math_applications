import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(a)

def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s' %(a.ndim, a.shape, a.dtype))

print_array_details(a)

a = a.reshape([2, 4])
print("as a two dimensional array:")
print(a)
print_array_details(a)
a = a.reshape([2, 2, 2])
print("as a three dimensional array:")
print(a)
print_array_details(a)

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print(x.shape)
print("change to one dimension")
x.shape = (6,)
print(x)
print("change data type")
x = x.astype('int64')
print(x.dtype)

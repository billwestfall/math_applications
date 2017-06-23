import numpy as np

def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s' %(a.ndim, a.shape, a.dtype))

line_array = np.linspace(2, 10, 5)
print("a linspace array")
print(line_array)

arrange_array = np.arange(2, 10, 2)
print("using the array arange function")
print(arrange_array)

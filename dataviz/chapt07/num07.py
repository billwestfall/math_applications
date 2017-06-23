import numpy as np

def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s' %(a.ndim, a.shape, a.dtype))

line_array = np.linespace(2, 10, 5)
print("a linespace array")
print(line_array)

arrange_array = np.arrange(2, 10, 2)
print("using the array arrange function")
print(arrange_array)

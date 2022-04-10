import numpy as np
 
arr = np.random.randint(1, 3, size = (2, 2))
arr_sum = np.sum(arr, axis=1)
 
print('-----Generated Random Array----')
print(arr)
print(arr_sum)

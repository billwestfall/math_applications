import numpy as np
 
arr = np.random.randint(1, 3, size = (2, 2))
arr_sum = np.sum(arr, axis=1)
arr_sumb = np.sum(arr, axis=0)
 
print('-----Generated Random Array----')
print(arr)
print(arr_sum)
print(arr_sumb)

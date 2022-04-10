import numpy as np

a1 = [3 3]
arr = np.random.randint(1, 3, size = (2, 2))
arr_sum = np.sum(arr, axis=1)
arr_sumb = np.sum(arr, axis=0)
 
print('-----Generated Random Array----')
print(arr)

if arr_sumarray_equal(a1):
 print(arr_sum)
else:
 print("Not sudoku")
print(arr_sum)
print(arr_sumb)

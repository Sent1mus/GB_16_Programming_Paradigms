import numpy as np

array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
array2 = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

correlation = np.corrcoef(array1, array2)[0,1]
print(correlation)
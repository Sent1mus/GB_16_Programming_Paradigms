import pandas as pd

array1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
array2 = pd.Series([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

correlation = array1.corr(array2)
print(correlation)
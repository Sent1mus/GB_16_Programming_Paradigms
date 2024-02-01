from scipy.stats import pearsonr

array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

correlation, _ = pearsonr(array1, array2)
print(correlation)
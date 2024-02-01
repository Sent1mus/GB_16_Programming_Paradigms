import statistics
import math

array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

m_x = statistics.mean(array1)
m_y = statistics.mean(array2)

if len(array1) != len(array2):
    print("Arrays are not of equal length.")
else:
    numerator = sum((array1[i] - m_x) * (array2[i] - m_y) for i in range(len(array1)))
    denominator = math.sqrt(sum((array1[i] - m_x) ** 2 for i in range(len(array1))) *
                            sum((array2[i] - m_y) ** 2 for i in range(len(array2))))

    correlation = numerator / denominator
    print(correlation)

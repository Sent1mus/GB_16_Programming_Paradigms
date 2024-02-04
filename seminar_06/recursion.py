# Бинарный поиск рекурсией
def binary(array, element):
    if not array:
        return -1
    mid = len(array) // 2
    if array[mid] == element:
        return mid
    elif array[mid] > element:
        result = binary(array[:mid], element)
        if result == -1 or result >= len(array):
            return -1
        else:
            return result
    else:
        result = binary(array[mid + 1:], element)
        if result == -1 or result >= len(array):
            return -1
        else:
            return result + mid + 1


array = [1, 3, 4, 6, 7, 8, 10, 13, 14, 16]
element = 4
index = binary(array, element)
print(index)

def binary(array, element):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (right + left) // 2
        if array[mid] < element:
            left = mid + 1
        elif array[mid] > element:
            right = mid - 1
        else:
            return mid
    return -1


array = [1, 3, 4, 6, 7, 8, 10, 13, 14]
element = 4
index = binary(array, element)

if index != -1:
    print("Element is present at index", str(index))
else:
    print("Element is not present in array: -1")

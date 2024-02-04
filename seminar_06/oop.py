class BinarySearch:
    def __init__(self, sorted_array):
        self.sorted_array = sorted_array

    def binary_search(self, target):
        low = 0
        high = len(self.sorted_array) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.sorted_array[mid] == target:
                return mid
            elif self.sorted_array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return None


array = [1, 3, 4, 6, 7, 8, 10, 13, 14, 16]
element = 4
binary_search = BinarySearch(array)
index = binary_search.binary_search(element)
if index is not None:
    print(f"Element found at index {index}")
else:
    print("Element not found")

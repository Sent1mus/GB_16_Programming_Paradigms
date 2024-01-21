import timeit


# Императивный код здесь
def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        max_index = i
        for j in range(i + 1, len(numberqs)):
            if numbers[max_index] < numbers[j]:
                max_index = j
        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]
    return numbers


# Декларативный код здесь
def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


list1 = [1, 3, 5, 2, 4, 6, -1, 0, -2]
print(sort_list_imperative(list1))  # [6, 5, 4, 3, 2, 1, 0, -1, -2]
print(sort_list_declarative(list1))  # [6, 5, 4, 3, 2, 1, 0, -1, -2]


def measure_time(sort_func, arr):
    start_time = timeit.default_timer()
    sort_func(arr)
    end_time = timeit.default_timer()
    return end_time - start_time


imperative_time = measure_time(sort_list_imperative, list1)
declarative_time = measure_time(sort_list_declarative, list1)

print(f"Imperative sort time: {imperative_time} seconds")       # Imperative sort time:  0.0000029 seconds
print(f"Declarative sort time: {declarative_time} seconds")     # Declarative sort time: 0.0000005 seconds

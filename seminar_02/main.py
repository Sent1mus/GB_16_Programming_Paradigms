# Структурная парадигма
n1 = int(input("Enter number1: "))
for i in range(1, n1 + 1):
    for j in range(1, n1 + 1):
        result = i * j
        print(f"{i} * {j} = {result}")
    print("")


# Процедурно + структурная
def get_multiply_table(n2):
    for i in range(1, n2 + 1):
        for j in range(1, n2 + 1):
            result = i * j
            print(f"{i} * {j} = {result}")
        print("")


n2 = int(input("Enter number2: "))
get_multiply_table(n2)
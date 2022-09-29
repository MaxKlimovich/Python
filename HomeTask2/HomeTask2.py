# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]


n = int(input("Enter the number: "))
4
def factorial(n):
    count = 1
    for i in range(1, n + 1):
        count *= i
    return count

a = [factorial(x) for x in range(1, n + 1)]
print(f'- {n} -> {a}')

# a = []
# for x in range(1, n + 1):
#     a.append(factorial(x))
# print(a)


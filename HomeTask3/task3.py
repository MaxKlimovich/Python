
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: '))

binary_string = ''
while n > 0:
    binary_string = str(n % 2) + binary_string
    n //= 2
print(binary_string)
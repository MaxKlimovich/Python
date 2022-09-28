
# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27


num = float(input('Enter the number: '))
n = len(str(num)) -1
number = int(num * 10 ** n)
sum = 0
while (number != 0):
    sum = sum + number % 10 
    number = number // 10
print(sum)
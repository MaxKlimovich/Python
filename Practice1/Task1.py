# 1. Напишите программу, которая принимает на вход два числа
#    и проверяет, является ли одно число квадратом другого.

x = int(input("введите первое число: "))
y = int(input("введите второе число: "))

if x == y ** 2 or y == x ** 2:
    print("Да")
else:
    print("нет")

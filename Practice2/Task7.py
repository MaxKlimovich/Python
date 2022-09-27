# Напишите программу, которая на вход принимает число N
# и выдает последовательность из N членов.

# from tkinter import N


# n = int(input('Enter the number'))
# m = 1

# for i in range(n):
#     print(m, end=',')
#     m *=-3

n = int(input("Enter the number"))

for i in range(n):
    print((-3) ** i, end=",")

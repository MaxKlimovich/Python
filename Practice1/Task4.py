# 4. Напишите программу, которая будет принимать на вход дробь
#    и показывать первую цифру дробной части числа.


n=float(input('введите число'))

a=int(n*10%10)

if a!=0:
    print(a)
else:
    print('no')
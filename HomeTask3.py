

# Напишите программу, которая принимает на вход 
# координаты точки (X и Y), причем X != 0 и Y != 0
# и выдает номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).


x = int(input('Введите первую точку x: '))
y = int(input('Введите вторую точку Y: '))

if x > 0 and y > 0:
    print (f'x = {x} y = {y} -> I quartet')
elif x < 0 and y > 0:
    print (f'x = {x} y = {y} -> II quartet')
elif x < 0 and y < 0:
    print (f'x = {x} y = {y} -> III quartet')
elif x > 0 and y < 0:
    print (f'x = {x} y = {y} -> VI quartet')
else:
    print ('on the coordinate axis!')
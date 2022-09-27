


# Напишите программу, которая по заданному
# номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).


a = int(input('ask number of quartal: '))

if  a == 1:
    print (f'1 quartal is locate -> (x > 0, y > 0)')
elif a == 2: 
    print (f'2 quartal is locate -> (x < 0, y > 0)')
elif a == 3:
    print (f'3 quartal is locate -> (x < 0, y < 0)')
elif a == 4:
    print (f'4 quartal is locate -> (x > 0, y < 0)')
else:
    print ('It is beyond my strength!')
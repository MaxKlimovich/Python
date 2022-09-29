# Типы данных и переменные
# int, float, boolean, str, list, None


# value = None
# print(type(value))
# print(type(a))
# print(type(b))
# a = 123
# b = 3.5
# value = 1321
# print(type(value))

# s = 'hello world'
# s = 'hello \nworld' #\n - означает перенос на другую строку

# print(s) #вывод строки
# print (a, b, s)
# print (a, '-', b, '-', s )
# print ('{2} - {1} - {0}' .format(a,b,s)) #ФОРМАТ (Можно выводить индексами, тоесть менять порядок)
# print (f'{a} - {b} - {s}')  #инторполяция


# Логическая переменная (Правда или Лож)
# t = True
# f = False
# print(t)
# print(f)

# Работа с массивами
# list = [1,2,3,4]
# col = [1.5, 'Text', True]
# print(list)
# print(col)

# Ввод и вывод данных
# print() Отдает данные
# input() Принимает данные

# print('Enter a data text')
# a = input()
# print('Enter b data text')
# b = input()
# print(a,b)
# print ('{1} {0}' .format(a,b))
# print (f'{a} {b}')


# Для того чтоб произвести решение необходимо обозначать тип значения

# print('Enter a data text')
# a = float(input())
# print('Enter b data text')
# b = int(input())
# print (f'{a} + {b} = {a+b}')


# Арифметические операции
# +       |  -        |  *        |  /      |  %                 |  //                                 |  **
# сложение|  вычитание|  умножение|  деление|  остаток от деления|  деление на целое                   |  Возведение в степень
#                                                                   (округленное до наименьшего целово)|  а в степени b
# (унарный + и -),
# () Меняют приоритет, Cокращение операции

# a = +123
# b = -231
# c = a+b
# print(c)

# a = 1.33232323
# b = 3
# c = round(a * b, 5) #Round указывает какое количество цифр будет после запятой
# print(c)


# a = 3
# a *= 5
# print(a)


# Логические операции

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# funk = 1
# t = 2
# x = 123
# print(funk<t<x)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]
# print(f)
# print(not 2 in f or 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)


# Управление конструкции if, if-else

# username = input('напишите имя: ')
# if (username == 'маша'):
#     print('Приветусики', username)
# else:
#     print('Здарова', username)


# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print (b)


# elif проверяем постоянно

# username = input('напишите ваше имя: ')
# if (username == 'Маша'):
#     print(f'{username} здарова!))')
# elif (username == 'Варя'):
#     print(f'Дорогая ты моя {username}!))')
# elif (username == 'Саня'):
#     print(f'Красава {username}!))')
# elif (username == 'Макс'):
#     print(f'А да код написал этот {username}!))')
# else:
#      print(f'Привет {username}!))')


# wile цикл!!!!!

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('О ЩИТ')
# print(inverted)


# for цикл!!!


# for i in 1, 2, 3, 4, 5, 6:
#     print(i**2)


# list = [1,2,3,4,5,6]
# for i in list:
#     print(i)

# from curses.ascii import islower


# r = range(1, 10, 2)  # итерируемый обьект
# for i in r:
#     print(i)


#!!!!!!Строки!!!!!!!
# text = 'Посмотри наверх'
# print(len(text))                    # 39
# print('еще' in text)                # True
# print(text.isdigit())               # False
# print(text.islower())               # True
# print(text.replace('ещё', 'ЕЩË'))   #
# print(text[0])                      # П
# print(text[1])                      # о
# print(text(len(text)-1)             # х
# print(text[-5])                     # а
# print(text[:])                      # Print(text) FULL
# print(text[2:5])                    # смотр


# for c in text:
#     print(c)


#!!!!!!Списки!!!!!!!


# numbers = [1, 2, 3, 4, 5, 6, 7]
# print(numbers)                              #  [1, 2, 3, 4, 5, 6, 7]
# ran = range(1,6)
# print(type(ran))                            #  class 'range'>
# numbers = list(ran)
# print(type(numbers))                        #  <class 'list'>
# print(numbers)                              #  [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'Len = {len(numbers)} positions')    #  5 len
# print(numbers)                              #  [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)                                #  [20, 4, 6, 8, 10]
# print(numbers)                              #  [10, 2, 3, 4, 5]


#!!!!!!!Расширенный функционал работы со списками!!!!!!!!!


# colors = ["red", "green", "blue"]

# for e in colors:
#     print(e)                                        # red green blue

# for e in colors:
#     print(e * 2)                                    # redred greengreen blueblue

# colors.append("gray")                               # добавить в конец
# print(colors == ["red", "green", "blue", "gray"])   # True
# colors.remove("red")                                # del colors[0] # удалить элемент


#!!!!!!!!!Функции в Python!!!!!!!!!

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
    
arg = 2.3
# print(f(arg))
# print(type(f(arg)))
# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

from random import choices


def List(n, word):
    new_list = []
    for i in range(n):
        a = choices(word, k=3)
        new_list.append("".join(a))
    return new_list


def List_serch(my_list, key):
    if my_list.count(key) > 1:
        print("yes")
        n = my_list.index(key)
        print(my_list.index(key, n + 1))
    else:
        print(-1)

result = List(20, "abc")
print(result)
List_serch(result, input())
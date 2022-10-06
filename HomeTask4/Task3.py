
# 3 Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

first_list = list(map(int, input("Введите числа через пробел:\n").split()))
print("Исходный список: ", first_list)
new_list = []
[new_list.append(i) for i in first_list if i not in new_list]
print("Неповторяющиеся элементы исходного списка: ", new_list)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# 4 - [8, 9, 10, 10] => [80, 90];
# 5 - [3, 3, 6, 8, 4] => [12, 24, 36]

input_list = [int(input('Введите число: ')) for i in range(int(input('Введите количество элементов списка: ')))]

mult_list = []
for i in range (len(input_list) // 2 + len(input_list) % 2):
    mult_list.append(input_list[i] * input_list[len(input_list) - 1 - i])
print(mult_list)
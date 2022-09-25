


# Напишите программу, которая принимает на вход
# координаты двух точек и находит расстояние
# между ними в 2D пространстве


xA = int(input("Напишите коордионату точки xA: "))
yA = int(input("Напишите коордионату точки yA: "))

xB = int(input("Напишите коордионату точки xB: "))
yB = int(input("Напишите коордионату точки yB: "))

import math
ab = float(math.sqrt(((xB - xA) ** 2) + ((yB - yA) ** 2)))
a_float = ab
limited_float = round(a_float, 3)
print(limited_float)

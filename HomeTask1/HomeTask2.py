

# Дз2


# Напишите программу для проверки истинности 
# утверждения -(x V y V z) = - x ^ - y ^ - z
# для всех значений предикат.


for x in range(2):
    for y in range(2):
        for z in range(2):
            if not ((x or y or z) == (not x) and not y and not z):
                print (x, y, z)
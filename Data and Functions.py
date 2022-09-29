# with open('file.txt', 'a') as data:
#     data.write('Line2\n')
#     data.write('Line3\n')
#     data.write('Line14\n')
#     data.write('Line11\n')

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w') #r - дописываем, a - перезапись,
# data.writelines(colors) #разделителей не будет
# data.writelines('\nLine2\n') #\n - разделяет строки, пишется с новой строки!
# data.writelines('Line3\n')
# data.close()


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# exit()


#!!!!!!!!!Функции в Python!!!!!!!!!


# import SyntaksisPythone as k

# print(k.f(1))

#!!!!!!!!!Функции в Python22222!!!!!!!!!

# def concatenetion(*params):
#     res: str = ''
#     for item in params:
#         res += item
#     return res

# print(concatenetion('a', 's', 'd', 'f')) #print -> asdf


#!!!!!!!!!!КОРТЕЖИ!!!!!!!!!!!!

# a = (1, 4, 6, 2, 3)
# print(a)
# print(a[-2])
# a[0] = 12 #для кортежей не работает, они являются неизменным списком

# for item in a:
#     print(item)

#!!!!!!!!!!СЛОВАРИ!!!!!!!!!!!!

# dictionary = {}
# dictionary = \
#     {
#         'up' : '↑',
#         'left' : '←',
#         'down' : '↓',
#         'right' : '→',
#     }
# # print(dictionary) # {'up' : '↑', 'left' : '←', 'down' : '↓', 'right' : '→',}
# # print(dictionary['left']) #←
# #типы ключей могут отличаться

# # for k in dictionary.keys():
# #     print(k)

# for k in dictionary.values():
#     print(k)

#!!!!!!!!СПИСКИ!!!!!!!!!!!

# list1 = [1, 2, 3, 4, 5]
# list2 = list1


# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)



list1 = [1, 2, 3, 4, 5]

# print(len(list1)) 
# print(list1.pop()) 
# print(list1) 
# print(list1.pop()) 
# print(list1) 
# print(list1.pop()) 
# print(list1) 

#!!!!!!

# print(list1.pop(2)) 
# print(list1) 

#!!!!!!!!

# print(list1.insert(2, 11)) 
# print(list1) 

#!!!!!!!!!

print(list1.append(11)) 
print(list1) 

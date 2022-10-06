




# List comprehansion

# list = []

# for i in range(1, 101):
#     # if(i%2 == 0):
#     list.append(i)
        
# print(list)


# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 11) if i%2 == 0]  # С использованием кортежей (i, f(i)) число и число в кубе (2, 8)
# print(list)


# def f(x):
#     return x**2

# list = [(i, f(i)) for i in (1, 2, 3, 5, 8, 15, 23, 38, 52) if i%2 == 0]
# print(list)



# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1,2,3,5,8,15,23,38,52' .split()

# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)


# !!!!!!!!!!!!!!!!!!!!Function MAP


# li = [x for x in range(1, 20)]
# li = list (map(lambda x: x+10, li))
# print(li)


# data = list(map(int,input().split()))
# print(data)



# data = map(int,'1 2 3 5 66 83 2'.split())
# print(data)

# for e in data:
#     print(e*10)


# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1,2,3,5,8,15,23,38,52' .split()

# res = map(int, data)
# res = where(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


# !!!!!!!!!!!!!!!Function Filter

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)



# data = '1,2,3,5,8,15,23,38,52' .split()

# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)
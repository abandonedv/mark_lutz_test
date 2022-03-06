# №1
# i = int(input("Введите число столбцов: "))
# j = int(input("Введите число строк: "))
#
# l = []
# for a in range(j):
#     l.append(i * [0])
#
# print(l)
#
# for a in range(j):
#     for b in range(i):
#         l[a][b] = input("Введите число: ")
#
# print(l)
#
# if i == j:
#     for a in range(i):
#         l[a][a] = 0
#
# print(l)


# №2
# d = {}
# d["fetf"] = 12
# print(d)
# def myenumerate(a):
#     n = 0
#     for e in a.keys():
#         yield n, e, a[e]
#         n += 1
#
#     it = myenumerate(d)
#     for i in range(len(d)):
#         print(next(it))
#


# №3
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
i = 3  # int(input("Введите число столбцов: "))
j = 3  # int(input("Введите число строк: "))

# l = []
# for a in range(j):
#     l.append(i * [0])

print(l)


# for a in range(j):
#     for b in range(i):
#         l[a][b] = int(input("Введите число: "))
#
# print(l)

def myf(x, a, b):
    for i in range(a):
        for j in range(b):
            yield i, j, x[i][j]


it = myf(l, j, i)

for i in range(i * j):
    print(next(it))

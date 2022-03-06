# class descr:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.__name] = value
#
#
class Matrix:
    #     h = descr()
    #     w = descr()
    #     m = descr()

    @staticmethod
    def fillmtr(w, h):
        a = []
        for i in range(w):
            b = []
            for j in range(h):
                b.append(j + 6 - i)
            a.append(b)
        return a

    def __init__(self, row=0, col=0, m=0):
        if isinstance(row, int):
            self.__row = row
        else:
            raise AttributeError
        self.__col = col
        if not m:
            self.__m = Matrix.fillmtr(row, col)
        else:
            self.__m = m

    def __add__(self, other):
        a = []
        for i in range(self.__row):
            b = []
            for j in range(self.__col):
                b.append(self.__m[i][j] + other.__m[i][j])
            a.append(b)
        return Matrix(self.__row, self.__col, a)

    def __mul__(self, other):
        t = []
        tq = []
        s = 0
        for i in range(self.__row):
            for j in range(other.__col):
                for k in range(other.__row):
                    s = s + self.__m[i][k] * other.__m[k][j]
                t.append(s)
                s = 0
            tq.append(t)
            t = []
        return Matrix(self.__row, other.__col, tq)

    def __eq__(self, other):
        for i in range(self.__row):
            for j in range(self.__col):
                if not (self.__m[i][j] == other.__m[i][j]):
                    return False
        return True

    def __setitem__(self, key, value):
        i, j = key.split()
        self.__m[int(i) - 1][int(j) - 1] = value

    def showmtr(self):
        for i in range(self.__row):
            print("\n")
            for j in range(self.__col):
                print("%5i" % self.__m[i][j], end="")
        print("\n")
        print(f"Строчек {self.__row}, Столбцов {self.__col}")

    def __repr__(self):
        Matrix.showmtr(self)
        return ""


a = Matrix(4, 3)
b = Matrix(4, 3)
c = Matrix(3, 6)
print(a)
print(b)
# a.showmtr()
t1 = a + b
print(t1)
print(a)
print(c)
t2 = a * c
print(t2)
print(a == b)
a["1 2"] = 2
print(a)
print(a == b)

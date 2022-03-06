class c(object):  # Новый стиль: Python З.Х и 2.Х
    data = 'spam'

    def __getattr__(self, name):  # Перехватывать нормальные имена
        print('getattr: ' + name)
        return getattr(self.data, name)

    def __getitem__(self, i):  # Переопределить встроенные операции
        print('getitem: ' + str(i))
        return self.data[i]  # Выполнить выражение или getattr

    def __add__(self, other):
        print("add: " + other)
        x = getattr(self.data, "__add__")
        print(x)
        return x(other)

    @staticmethod
    def gg():
        print("gg")


x = c()
y = c()
x.data.__add__("ded")
print(type(x).gg())
print("dfd".upper())
print(id(x))
print(x.upper)
print(y.upper)
print(x.upper())
print(x[1])
print(type(x).__getitem__(x, 1))
print(x.__add__("eggs"))
print(type(x).__add__(x, "eggs"))



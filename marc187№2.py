import random

def square(arg):
    return arg ** 2  # Простые функции (def или lambda)


class Sum:
    def __init__(self, val):  # Вызываемые экземпляры
        self.val = val

    def __call__(self, arg):
        return self.val + arg


class Product:
    def __init__(self, val):  # Связанные методы
        self.val = val

    def method(self, arg):
        return self.val * arg


class Negate:
    def __init__(self, val):  # Классы также являются вызываемыми объектами
        self.val = -val  # Но вызываются для создания объектов,

    # не для выполнения работы
    def __repr__(self):  # Формат вывода экземпляров
        return str(self.val)


sobject = Sum(2)
pobject = Product(3)
actions = [square, sobject, pobject.method, Negate]
x = 0
table = {random.randrange(1, 66): act for act in actions}
table2 = {(act for act in actions) : random.randrange(1, 66)}
print(table2.items())
for (key, value) in table.items():
    print("{0} => {1}".format(key, value))

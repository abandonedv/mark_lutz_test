import math


class Table:

    def __repr__(self):
        return str(self.__dict__)


class Round(Table):
    def __init__(self, r=None):
        self.r = r

    def Square(self):
        return math.pi * self.r ** 2


class Rect(Table):
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def Square(self):
        return self.a * self.b


y = Round(5)
print(y)
print(y.Square())

t = Rect(2, 6)
print(t)
print(t.Square())

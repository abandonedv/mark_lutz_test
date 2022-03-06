import math

class Table:

    def __init__(self, *args):
        self.values = args

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

a = Round(5)
print(a)
print(a.Square())

b = Rect(2, 6)
print(b)
print(b.Square())
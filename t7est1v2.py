from math import pi


class Table:
    def __init__(self, *args):
        self.v = args


class Round(Table):
    def Square(self):
        r, = self.v
        return pi * r ** 2


class Rect(Table):
    def Square(self):
        a, b = self.v
        return a * b


t1 = Round(9)
print(t1.Square())

t2 = Rect(2, 9)
print(t2.Square())
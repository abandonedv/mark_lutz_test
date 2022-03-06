import math


class point2D:
    __slots__ = ("x", "y", "__length")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = math.sqrt(x * x + y * y)
    #   self.length = self.__length
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


f = point2D(5, 7)
print(f.__slots__)// flask
// парсинг
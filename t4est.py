class CoordValue:

    def __set_name__(self, owner, name):
        print("setname: ", self, owner, name, sep=" ||| ")
        self.__name = name

    def __get__(self, instance, owner):
        print("get: ", self, instance, owner, sep=" ||| ")
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value
        print("set: ", self, instance, value, sep=" ||| ")

    # def __delete__(self, instance):
    #     del self.__value


class Point:
    __coordx = CoordValue()
    coordy = CoordValue()
    coordx1 = CoordValue()
    coordy1 = CoordValue()

    def __init__(self, x=0, y=0, x1=0, y1=0):
        self.__coordx = x
        self.coordy = y
        self.coordx1 = x1
        self.coordy1 = y1

    def __repr__(self):
        return str(self.__dict__)

    # def __checkValue(x):
    #     return isinstance(x, int) or isinstance(x, float)
    #
    # @property
    # def coord(self):
    #     return self.__x
    #
    # @coord.setter
    # def coord(self, x):
    #     if Point.__checkValue(x):
    #         self.__x = x
    #     else:
    #         raise ValueError
    #
    # @coord.deleter
    # def coord(self):
    #     del self.__x
    #     print("Удалено!")



a = Point(1, 2, 3, 4)
# print(a)
a.coordy = 3
# print(a.coordx1)
# print(a)
# b = Point(4, 6, 66, 7)

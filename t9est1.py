class Test:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    def __add__(self, other):
        return self.__x + other.__x, self.__y + other.__y, self.__z + other.__z

    def __sub__(self, other):
        return self.__x - other.__x, self.__y - other.__y, self.__z - other.__z

    def __mul__(self, other):
        return self.__x * other.__x, self.__y * other.__y, self.__z * other.__z

    def __truediv__(self, other):
        return self.__x / other.__x, self.__y / other.__y, self.__z / other.__z

    def __lt__(self, other):
        return self.__x < other.__x and self.__y < other.__y and self.__z < other.__z

    def __gt__(self, other):
        return self.__x > other.__x and self.__y > other.__y and self.__z > other.__z

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y and self.__z == other.__z

    def __getitem__(self, item):
        if item == "x":
            return self.__x
        elif item == "y":
            return self.__y
        elif item == "z":
            return self.__z

    def __setitem__(self, key, value):
        if key == "x":
            self.__x = value
        elif key == "y":
            self.__y = value
        elif key == "z":
            self.__z = value

    def __repr__(self):
        return str(self.__dict__)


a = Test(2, 2, 2)
b = Test(4, 3, 25)
print(a)
print(b)
print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a < b)
# print(a > b)
print(a["x"])
a["x"] = 1
print(a)

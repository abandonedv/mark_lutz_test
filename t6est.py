class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self.__dict__)

class TwoPoints(Point):
    def __init__(self, sp: Point, ep: Point, colour=None, width=1):
        self._sp = sp
        self._ep = ep
        self._colour = colour
        self.__width = width


class Line(TwoPoints):
    pass

class Rec(TwoPoints):
    pass




s = Point(1, 3)
print(s)
e = Point(4, 6)
print(e)
result = Line(s, e, "white", 2)
print(result)

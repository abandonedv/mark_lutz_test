class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class cpPoint(Point):
    def __init__(self, el=Point()):
        self.x = el.x
        self.y = el.y


a = Point(1, 2)

b = cpPoint()
print(b.__dict__)
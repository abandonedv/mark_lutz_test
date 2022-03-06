class Point:
    lst1 = []
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.lst1.append(self)

    def show(self):
        print(self.x, self.y)


lst = []

n = 5
for i in range(n):
    x = Point(i, i)
    lst.append(x)
    n -= 1

for i in lst:
    Point.show(i)

print(lst)
print(Point.lst1)
for x in Point.lst1:
    print(x.__dict__)

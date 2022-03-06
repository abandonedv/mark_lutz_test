class D:
    __slots__ = ["a", "b", "__dict__"]
    с = 3

    def __init__(self):
        self.d = 4


x = D()
x.a = 2
x.b = 5
x.c = 5
# for attr in list(getattr(x, "__dict__", [])) + getattr(x, "__slots__", []):
#     print(attr, getattr(x, attr))

for attr in list(x.__dict__) + x.__slots__:
    if attr != "__dict__":
        print(attr, getattr(x, attr))

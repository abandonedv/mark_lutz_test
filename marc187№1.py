import ctypes.wintypes


class Number:
    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2

    def triple(self):
        return self.base * 3

    @staticmethod
    def a():
        print(2)


x = Number(2)
y = Number(3)
z = Number(4)
x.double()
acts = [x.double, y.double, y.triple, z.double]
for act in acts:  # Вызовы откладываются
    print(act())

bound = x.double
bound2 = y.double
bound3 = Number.a
print(bound.__self__, bound.__func__)
print(bound.__self__.base)
print(bound())

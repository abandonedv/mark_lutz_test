class Metaclass(type):
    def __new__(meta, clsname, supers, attrdict):
        print("In M.__new__ : ")
        print([clsname, supers, list(attrdict.keys())])
        return type.__new__(meta, clsname, supers, attrdict)


def decorator(cls):
    return Metaclass(cls.__name__, cls.__bases__, dict(cls.__dict__))


class A:
    x = 1


@decorator
class B(A):
    y = 2

    def m(self):
        return self.x + self.y


print(B.x)
print(B.y)
print(B.__class__)
I = B()
print(I.x, I.y, I.m())

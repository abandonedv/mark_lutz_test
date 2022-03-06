class Test:
    d = {1: "fretg", "feref": 234.21}

    def __init__(self):
        self.__dict__ = Test.d

a = Test()
print(a.__dict__)
b = Test()
print(b.__dict__)
a.d.popitem()
print(a.__dict__)
print(b.__dict__)
class A:
    pass

class tracer:
    def __init__(self, func):  # При декорировании @
        self.calls = 0  # Сохранение функции для вызова в будущем
        self.func = func

    def __call__(self, *args, **kwargs):  # При обращении к исходной функции
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


def spam(a, b, c):
    print(a + b + c)

s = A()
spam = tracer(spam)
print(spam, s)
spam(1, 2, 3)
spam(a=4, b=5, c=6)

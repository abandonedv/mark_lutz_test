class tracer:
    def __init__(self, func):  # При декорировании @
        self.calls = 0  # Сохранение функции для вызова в будущем
        self.func = func

    def __call__(self, *args, **kwargs):  # При обращении к исходной функции
        print(id(self))
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):  # giveRaise = tracer (giveRaise)
        self.pay *= (1.0 + percent)

    giveRaise = tracer(giveRaise)
    print(id(giveRaise))

    def lastName(self):  # lastName = tracer(lastName)
        return self.name.split()[-1]

    lastName = tracer(lastName)
    print(id(lastName))


bob = Person('Bob Smith', 50000)
print(id(bob))
bob.giveRaise(.25)
print(bob.lastName())

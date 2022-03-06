class Person:
    def __init__(self, surname, forename, old):
        self.forename = forename
        self.surname = surname
        self.old = old

    def __repr__(self):
        return str(self.__dict__)


class LOP:
    def __init__(self, l):
        self.l = l

    def __call__(self, *args, **kwargs):
        key, = args
        return sorted(self.l, key=lambda x: x.__dict__[key])


p = [Person("Иванов", "Иван", 56),
     Person("Петров", "Степан", 31),
     Person("Сидоров", "Альберт", 25)]

a = LOP(p)
print(a("old"))

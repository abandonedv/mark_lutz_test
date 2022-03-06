def factory(aClass, *pargs, **kargs):  # Кортеж или словарь с переменным
    # количеством аргументов
    return aClass(*pargs, **kargs)  # Вызывает aClass (или apply в Python 2.X)


class Spam:
    def doit(self, message):
        print(message)


class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job


objectl = factory(Spam)  # Создать объект Spam
object2 = factory(Person, "Arthur", "King")  # Создать объект Person
objects = factory(Person, name="Brian")  #
print(objectl.__dict__)
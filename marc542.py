class Tracer:
    def __init__(self, aClass):
        self.aClass = aClass

    def __call__(self, *args):
        print(id(self))
        self.wrapped = self.aClass(*args)
        print(id(self.wrapped))
        return self

    # При декорировании 0
    # Использование атрибуты экземпляра
    # При создании экземпляров
    # ОДИН (ПОСЛЕДНИЙ) ЭКЗЕМПЛЯР НА КЛАСС!
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)

    def __repr__(self):
        return str(self.__dict__)


@Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)


@Tracer
class Person:  #
    def __init__(self, name):  #
        self.name = name

    def __repr__(self):
        return str(self.__dict__)

bob = Person("Bob")
print(bob)
print(bob.name)
sue = Person("Sue")
print(sue)
print(sue.name)
print(bob)
print(bob.name)

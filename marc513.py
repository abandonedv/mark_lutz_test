def decorator(cls):  # При декорировании @
    class Wrapper:
        def __init__(self):  # При создании экземпляров
            self = cls()
            print("Wrapper: %i" % id(self))
            # print(self.attr2)
            print(self.__dict__)

        def __getattr__(self, name):  # При извлечении атрибутов
            return getattr(self.wrapped, name)

        def __repr__(self):
            return str(self.__dict__)

    return Wrapper


@decorator
class C:  # C = decorator(C)
    def __init__(self):  # Запускается методом Wrapper,__init__
        print("Class: %i" % id(self))
        self.attr = "spam"

    def __repr__(self):
        return str(self.__dict__)


x = C()
print("X: %i" % id(x))# В действительности вызывается Wrapper (6 , 1)
print(x.__dict__)
print(x)

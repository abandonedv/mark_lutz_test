def Tracer(classname, supers, classdict):  # При вызове, создающем класс
    aClass = type(classname, supers, classdict)  # Создание клиентского класса

    class Wrapper:
        def __init__(self, *args, **kargs):  # При создании экземпляров
            self.wrapped = aClass(*args, **kargs)

        def __getattr__(self, attrname):
            print('Trace: ', attrname)  # Перехват всех атрибутов
            # кроме . wrapped
            return getattr(self.wrapped, attrname)  # Делегирование внутреннему

        def __repr__(self):
            return str(self.__dict__)

    # объекту
    return Wrapper


class Person(metaclass=Tracer):  # Создание Person c Tracer
    def __init__(self, name, hours, rate):  # Wrapper запоминает Person
        self.name = name
        self.hours = hours
        self.rate = rate  # Извлечение внутри методов не отслеживается

    def pay(self):
        return self.hours * self.rate

    def __repr__(self):
        return str(self.__dict__)


bob = Person('Bob', 40, 50)  # bob - на самом деле экземпляр Wrapper
print(type(Person))  # Wrapper содержит внедренный экземпляр Person
print(bob)

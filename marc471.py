class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel  # Сохранить несвязанный метод
        self.__doc__ = doc  # или другие вызываемые объекты

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")  # нельзя извлечь атрибут
        return self.fget(instance)  # Передать instance экземпляру self

    # в методах доступа к свойствам
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")  # нельзя установить атрибут
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can* t delete attribute")  # нельзя удалить атрибут
        self.fdel(instance)


class Person:
    def getName(self):
        return self.__dict__["name"]

    def setName(self, value): self.__dict__["name"] = value

    name = Property(getName, setName)  # Использовать подобно property ()


x = Person()
x.name = 'Bob'
y = Person()
y.name = "Carl"
print(x.name)
print(y.name)
print(x.__dict__)


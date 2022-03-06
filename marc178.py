class Wrapper:
    def __init__(self, object):
        self.wrapped = object  # Сохранить объект

    def __getattr__(self, attrname):
        print('Trace: ' + attrname)  # Трассировать извлечение
        return getattr(self.wrapped, attrname)


x = Wrapper([1, 2, 3])  # Создать оболочку для списка
x.append(4)
print(x.wrapped)
x = Wrapper({"а": 1, "b": 2})  # Создать оболочку для словаря
list(x.keys())
print(x.wrapped)

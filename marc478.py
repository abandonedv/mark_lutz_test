class Person:  # Код переносимый: Python 2.Х или З.Х
    def __init__(self, name):  # При [PersonO ]
        self._name = name  # Запускается__ setattr__ !
    #
    # def __getattr__(self, attr):  # При [obj.неопределенный_атрибут]
    #     print("get: " + attr)
    #     if attr == 'name':  # Перехват имени name: не хранится в экземпляре
    #         return self._name  # Зацикливания нет: реальный атрибут
    #     else:  # Остальные являются ошибками
    #         raise AttributeError(attr)

    def __getattribute__(self, attr):  # При [obj .любой_атрибут]
        print('get: ' + attr)
        if attr == 'name':  # Перехват всех имен
            attr = '_name'  # Отображение на внутреннее имя
        return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value):
        print("set: " + attr)
        if attr == ' name ':
            attr = '_name'
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        print('del: ' + attr)
        if attr == ' name ':
            attr = '_name'
        del self.__dict__[attr]


bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name
print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)
# print(Person.name._ doc__ )

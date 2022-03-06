class Person:
    def __init__(self, name):
        self._name = name

    class Name:  # Использование вложенного класса
        "name descriptor docs"



        def __get__(self, instance, owner):
            print("fetch. . . ")
            return instance._name

        def __set__(self, instance, value):
            print('change...')
            instance.__dict__["пе"] = value

        def __delete__(self, instance):
            print('remove...')
            del instance._name

    name = Name()
    surname = Name()

a = Person("Mike")
a.surname = "V."
print(a.__dict__)
b = Person("Bob")
print(b.__dict__)
print(a.__dict__)

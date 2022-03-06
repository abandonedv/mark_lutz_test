class CardHolder(object):  # В Python 2.Х требуется (object)
    acctlen = 8  # Данные класса
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct  # Данные экземпляра
        self.name = name  # Тоже запускают методы__set__ !
        self.age = age  # Имя X не требуется: в дескрипторе
        self.addr = addr  # Имя addr не является управляемым

    # remain не имеет данных
    class Name(object):
        def __get__(self, instance, owner):  # Имена классов: локальные в CardHolder
            return instance.__dict__["name"]

        def __set__(self, instance, value):
            value = value.lower().replace(" ", '_')
            instance.__dict__["name"] = value

    name = Name()

    class Age(object):
        def __get__(self, instance, owner):
            return instance.__dict__["age"]  # Использовать данные дескриптора

        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')  # недопустимый возраст
            else:
                instance.__dict__["age"] = value

    age = Age()

    class Acct(object):
        def __get__(self, instance, owner):
            return instance.__dict__["name"] + '***'

        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:  # Использовать данные
                # экземпляра класса
                raise TypeError('invald acct number')  # недопустимый номер счета
            else:
                instance.__dict__["acct"] = value

    acct = Acct()

    class Remain(object):
        def __get__(self, instance, owner):
            return instance.retireage - instance.age  # Запускается Age.__ get__

        def __set__(self, instance, value):
            raise TypeError("cannot set remain")  # Установка не разрешена

    remain = Remain()

    def __repr__(self):
        return str(self.__dict__) + str(self.remain)


if __name__ == '__main__':
    bob = CardHolder("1234-5678", 'Bob Smith', 40, '123 main st')
    print(bob)
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    print(bob)
    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    print(sue)
    try:
        sue.age = 200
    except:
        print("Bad age for Sue")  # Недопустимый возраст для sue
    try:
        sue.remain = 5
    except:
        print("Can’t set sue.remain")  # Невозможно установить sue.remain
    try:
        sue.acct = "1234567"
    except:
        print("Bad acct for Sue")

class CardHolder(object):  # В Python 2.X требуется (object)
    acctlen = 8  # Данные класса
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct  # Данные экземпляра
        self.name = name  # Тоже запускают__setattr__
        self.age = age  # Имя _acct не корректируется:
        # проверяется name
        self.addr = addr  # Имя addr не является управляемым
        # remain не имеет данных

    def __getattribute__(self, name):
        superget = object.__getattribute__  # Зацикливания нет:
        # на один уровень выше
        if name == "acct":  # При извлечении всех атрибутов
            return superget(self, "acct")[:-3]
        elif name == "remain":
            return superget(self, 'retireage') - superget(self, 'age')
        else:
            return superget(self, name)  # name, age, addr: хранятся

    def __setattr__(self, name, value):
        if name == 'name':  # При операциях присваивания всех атрибутов
            value = value.lower().replace(' ', '_')  # addr хранится напрямую
        elif name == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')  # недопустимый возраст
        elif name == 'acct':
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invald acct number')  # недопустимый номер счета
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value

    def __repr__(self):
        return str(self.__dict__) + str(self.remain)

if __name__ == '__main__':
    bob = CardHolder("1234-5678", 'Bob Smith', 40, '123 main st')
    print(bob)
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    print(bob.acct)
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
class CardHolder(object):  # В Python 2.Х требуется (object)
    acctlen = 8  # Данные класса
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct  # Данные экземпляра
        self.name = name  # Тоже запускают методы установки
        # свойств I
        self.age = age  # Имя__X корректируется, чтобы
        # содержать имя класса
        self.addr = addr  # Имя addr не корректируется
        # Свойство remain не имеет данных

    def getName(self):
        return self.__name

    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value

    name = property(getName, setName)

    def getAge(self):
        return self.__age

    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError("invalid age")  # недопустимый возраст
        else:
            self.__age = value

    age = property(getAge, setAge)

    def getAcct(self):
        return self.__acct[:-3] + '***'

    def setAcct(self, value):
        value = value.replace('-', "")
        if len(value) != self.acctlen:
            raise TypeError("invald acct number")  # недопустимый номер счета
        else:
            self.__acct = value

    acct = property(getAcct, setAcct)

    def remainGet(self):  # Могло быть методом, а не атрибутом,
        return self.retireage - self.age  # если только уже не используется

    remain = property(remainGet)

    def __repr__(self):
        return str(self.__dict__) + str(self.remain)
# как атрибут

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

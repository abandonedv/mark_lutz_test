class Human:
    """Человек, возраст которого не может быть больше 120 и меньше 0"""

    def __init__(self, age=0):
        self.age = age

    def getAge(self):
        return self.age

    def setAge(self, p):
        if 120 > p >= 0:
            self.__dict__["age"] = p
        else:
            self.__dict__["age"] = 0




a = Human(34)
a.age = 155
print(a.__dict__)
a.age = 54
print(a.__dict__)
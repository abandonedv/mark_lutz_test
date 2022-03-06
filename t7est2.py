class Animal:
    pass


class Dog(Animal):
    @staticmethod
    def say():
        print("gav")


class Cat(Animal):
    @staticmethod
    def say():
        print("mew")


for x in (Dog(), Cat()):
    x.say()

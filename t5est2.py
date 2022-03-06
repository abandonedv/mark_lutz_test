class Dog:
    count = 0

    def __new__(cls, *args, **kwargs):
        print(cls, *args, **kwargs, sep=" ||| ")
        if Dog.count <= 4:
            print(Dog.count)
            return super(Dog, cls).__new__(cls)
        else:
            print("Все, хватит!")

    def __init__(self, name=None, age=None, poroda=None):
        self.name = name
        self.age = age
        self.poroda = poroda
        Dog.count += 1


for i in range(7):
    print(Dog().__dict__)
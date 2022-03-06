from marc80 import AttrDisplay


class Person(AttrDisplay):

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def giveraise(self, percent=10):
        self.pay = self.pay + percent * 0.01 * self.pay
        return self.pay

    # def __repr__(self):
    #     return "[Person: %s %s %s]" % (self.name, self.job, self.pay)


class Manager(Person):

    def __init__(self, name, pay):
        Person.__init__(self, name, "mng", pay)

    def giveraise(self, percent, bonus=10):
        Person.giveraise(self, percent + bonus)
        return self.pay


if __name__ == '__main__':
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100000)
    print(bob)
    print(sue)

    print(bob.lastname(), sue.lastname())
    print(sue.giveraise(20))
    print(sue)
    carl = Manager("Carl Whitney", 155)
    print(carl.giveraise(2, 5))
    print(carl.lastname())
    print(carl)

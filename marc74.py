from marc80 import AttrDisplay


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def giveraise(self, percent=10):
        self.pay = self.pay + percent * 0.01 * self.pay
        return self.pay

    def __repr__(self):
        return "[Person: %s %s %s]" % (self.name, self.job, self.pay)


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, "mng", pay)

    def giveraise(self, percent, bonus=1):
        self.person.giveraise(percent + bonus)

    def __getattr__(self, item):
        return getattr(self.person, item)

    def __repr__(self):
        return str(self.person)

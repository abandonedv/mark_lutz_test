class Iter:
    def __init__(self, obj):
        self.lim = len(obj.l)
        self.list = obj.l
        self.i = 0
        self.par = int(input("\n1 - Name"
                             "\n2 - Surname"
                             "\n3 - Age"
                             "\nYour choice: "))

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.lim:
            raise StopIteration
        else:
            self.i += 1
            return self.list[self.i - 1][self.par - 1]


class Visitors:
    def __init__(self, l=None):
        if l is None:
            self.l = []
        else: self.l = l

    def addv(self, person: str):
        x = tuple(person.split())
        self.l.append(x)

    def __iter__(self):
        return Iter(self)


d = Visitors()
d.addv("Mike T. 19")
d.addv("Carl P. 45")
d.addv("Tom D. 25")
d.addv("Mike Z. 16")

for x in d:
    print(x)
print(d.__dict__)

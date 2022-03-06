class Iter:
    def __init__(self, obj):
        self.lim = len(obj.l)
        self.l = obj.l

    def __iter__(self):
        return self

    def __next__(self):
        if self.lim <= 0:
            raise StopIteration
        else:
            self.lim -= 1
            return self.l[self.lim]


class List:
    def __init__(self, l=None):
        if l is None:
            l = []
        self.l = l

    def add(self, digit):
        self.l.append(digit)

    def __iter__(self):
        return Iter(self)

    def __repr__(self):
        return str(self.l)


q = List([1, 5, 7, 32, 0])
q.add(3)
print(q)

for a in q:
    print(a)

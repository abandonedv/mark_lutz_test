class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        self.data -= other

    def __add__(self, other):
        self.abc = other


x = Number(4)
x - 2
print(x.data)
x + 2
print(x.__dict__)
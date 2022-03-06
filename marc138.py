class Squares:
    def __init__(self, start, stop):  # Метод__ next__ является

        # автоматическим/подразумеваемым
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2


x = Squares(1, 5)
for i in x:
    print(i, end=' ')

for i in x:
    print(i, end=' ')

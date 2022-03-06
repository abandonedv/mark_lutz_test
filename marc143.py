class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, item):  # Запасной вариант для итерации
        print(' get [%s] : ' % item, end="")  # Также для индексирования, нарезания
        return self.data[item]

    # def __iter__(self):  # Предпочтительнее для итерации
    #     print(' iter=> ', end=" ")  # Допускает только один активный итератор
    #     self.ix = 0
    #     return self
    #
    # def __next__(self):
    #     print("next:", end="")
    #     if self.ix == len(self.data):
    #         raise StopIteration
    #     item = self.data[self.ix]
    #     self.ix += 1
    #     return item
    #
    # def __contains__(self, x):
    #     print("contains : ", end="")
    #     return x in self.data

    # next - __next__


if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)
    for i in X:
        print(i, end=' I ')
    # Предпочтительнее для операции in
    # Совместимость c Python 2.Х/З.Х
    # Создать экземпляр
    # Членство
    # Циклы for
    print()
    print([i ** 2 for i in X])
    print(list(map(bin, X)))
    I = iter(X)
    while True:
        try:
            print(next(I), end="")
        except StopIteration:
            break

class DefDict:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        print(id(self.__v))
        dict = {}
        dict.update(self.__v)
        print(id(dict), id(self.__v))
        self.__temp = dict
        print(id(self.__temp), id(self.__v))
        print(self.__v, self.__temp)
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(id(self.__temp), id(self.__v))
            self.__v = self.__temp
            print(id(self.__temp), id(self.__v))
        return True


d = {1: "regw", "e": 2.5, 4: "regw", "fgt": 2.5, 54: "regw", "tgr": 55}
x = DefDict(d)
with x as d2:
    for i in range(len(d2) + 1):
        d2.popitem()

print(d)

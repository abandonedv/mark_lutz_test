class Calendar:
    __slots__ = ["__day", "__month", "__year"]

    def __init__(self, day=None, month=None, year=None):
        self.__day = day
        self.__month = month
        self.__year = year

    def setData(self, day, month, year):
        if day > 31:
            self.__day = "Error"
        else:
            self.__day = day
        self.__month = month
        self.__year = year

    def getData(self):
        return self.__day, self.__month, self.__year

    day = property(getData, setData)


a = Calendar(1, "Jun", 2005)
print(a.getData())
a.setData(34, "Mar", 2016)
print(a.getData())


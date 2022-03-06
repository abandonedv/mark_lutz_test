class t3est:
    width = 0

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def setAttr(self, x, y):
        self.__x = x
        self.__y = y

    def getAttr(self):
        return self.__x, self.__y

    def __getattribute__(self, item):
        if item == "_t3est__x":
            return "Неа"
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "width":
            self.__dict__[key] = "booooooooooooom"
        else:
            self.__dict__[key] = value


pt = t3est(1, 2)
pt.setAttr(2, 3)
print(pt.getAttr())
print(t3est.__dict__)
pt.width = 10
print(t3est.__dict__)
print(pt.width)

class c1:
    def __init__(self, x=0):
        self.x = x


class c2(c1):
    def __init__(self, x, y=0):
        super(c2, self).__init__(x)
        self.y = y


class c3(c2):
    def __init__(self, x, z=0):
        super(c2, self).__init__(x)
        # c1.__init__(self, x)
        self.z = z


a = c3(1, 3)
print(a.__dict__)

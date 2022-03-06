class Rectangle:
    @staticmethod
    def S(width, height):
        return width * height

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.S = Rectangle.S(width, height)


r = Rectangle(9, 4)
print(r.__dict__)

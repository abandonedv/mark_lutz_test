class CoordError(Exception):
    pass


class ImageXIterator:
    def __init__(self, img, y):
        self.__limit = img.width
        self.__y = y
        self.__img = img
        self.__x = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__x >= self.__limit:
            raise StopIteration

        self.__x += 1
        return self.__img[self.__x - 1, self.__y]


class ImageYIterator:
    def __init__(self, eee):
        self.__limit = eee.height
        self.__img = eee
        self.__y = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__y >= self.__limit:
            raise StopIteration

        self.__y += 1
        return ImageXIterator(self.__img, self.__y - 1)


class Image:
    def __init__(self, width, height, background="_"):
        self.__background = background
        self.__pixels = {}
        self.__width = width
        self.__height = height
        self.__colors = {self.__background}

    def filterpix(self):
        for i in list(self.__pixels.keys()):
            # print(self.__pixels.keys())
            if i[0] > self.__width:
                self.__pixels.pop(i)
            elif i[1] > self.__height:
                self.__pixels.pop(i)

    def resize(self, width, height):
        w = self.width
        h = self.height
        self.__width = width
        self.__height = height
        if w != self.__width or h != self.__height:
            self.filterpix()

    def __repr__(self):
        return str(self.__dict__)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def __checkCoord(self, coord):
        if not isinstance(coord, tuple) or len(coord) != 2:
            raise CoordError

        if not (0 <= coord[0] < self.__width) or not (0 <= coord[1] < self.__height):
            raise CoordError

    def __setitem__(self, coord, color):
        self.__checkCoord(coord)

        if color == self.__background:
            self.__pixels.pop(coord, None)
        else:
            self.__pixels[coord] = color
            self.__colors.add(color)

    def __getitem__(self, coord):
        self.__checkCoord(coord)
        return self.__pixels.get(coord, self.__background)

    def __iter__(self):
        return ImageYIterator(self)


img = Image(20, 20)
img[14, 1] = "*"
img[10, 1] = "*"
img[1, 1] = "*"
img[1, 3] = "*"

for row in img:
    # print(row.__dict__)
    for pixel in row:
        print(pixel, sep=" ", end=" ")
    print()

img.resize(5, 30)

print(img.__dict__)
for row in img:
    # print(row.__dict__)
    for pixel in row:
        print(pixel, sep=" ", end=" ")
    print()


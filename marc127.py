class Indexer:
    def __getitem__(self, item):
        return item ** 2


x = Indexer()
for i in range(5):
    print(x[i], end=" ")
print("\n" + "=" * 100)


class Indexer2:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, item):
        print("getitem: ", item)
        return self.data[item]


x = Indexer2()
print(x[2:4])
print("=" * 100)


class Indexer3:
    def __getitem__(self, item):
        if isinstance(item, int):
            print("indexing", item)
        else:
            print("slicing", item.start, item.stop, item.step)


x = Indexer3()
x[99]
x[1:99:2]
x[1:]

class Slicer:
    def __getitem__(self, item):
        print(item)
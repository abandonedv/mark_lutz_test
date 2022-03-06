class DescSquare:
    def __init__(self, start):  # Каждый дескриптор имеет
        # собственное состояние
        self.value = start

    def __get__(self, instance, owner):  # При извлечении атрибута
        return self.value ** 2

    def __set__(self, instance, value):  # При присваивании атрибута
        self.value = value  # Операция удаления и строка
    # документации отсутствуют


class Client1:
    X = DescSquare(3)  # Присвоить экземпляр дескриптора атрибуту класса


class Client2:
    X = DescSquare(32)  # Еще один экземпляр в другом клиентском классе


# Можно было бы также предусмотреть
# два экземпляра в том же самом классе
c1 = Client1()
c2 = Client1()
print(c1.X)  # 3 ** 2
c1.X = 4
c2.X = 9
print(c1.X)
print(c2.X)

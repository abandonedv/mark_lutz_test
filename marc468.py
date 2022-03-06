class DescState:  # Использование состояния дескриптора, (object) в Python 2.Х
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print("DescState get")
        self.value = 10
        return self

    def __set__(self, instance, value):
        print("DescState set")
        self.value = value


# Клиентский класс
class CalcAttrs:
    X = DescState(2)
    print(X.__dict__)
    Y = 3

    def __init__(self):
        self.Z = 4
        # При извлечении атрибута
        # При присваивании атрибута
        # Атрибут класса дескриптора
        # Атрибут класса
        # Атрибут экземпляра


obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)  # X вычисляется, остальные нет
obj.X = 5  # Присваивание X перехватывается
CalcAttrs.Y = 6  # Y повторно присваивается в классе
obj.Z = 7  # Z присваивается в экземпляре
print(obj.X, obj.Y, obj.Z)
obj2 = CalcAttrs()
obj.X = 25
print(obj2.X, obj2.Y, obj2.Z)
print(obj.X, obj.Y, obj.Z)
print(CalcAttrs.X.__dict__)

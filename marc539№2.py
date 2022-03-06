class Wrapper:
    def __init__(self, object):
        self.wrapped = object  # Сохранение объекта

    def __getattr__(self, attrname):
        print("Trace: ", attrname)  # Отслеживание извлечения
        return getattr(self.wrapped, attrname)  # Делегирование извлечения


x = Wrapper([1, 2, 3])  # Оборачивание списка
print(x.append(4))  # Делегирование списковому методу
print(x.wrapped)  # Вывод элементов
х = Wrapper({"а": 1, "b": 2})  # Оборачивание словаря
print(list(х.keys()))

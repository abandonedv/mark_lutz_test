import random


class Tree:
    def __init__(self):
        self.data = 1
        self.son = None
        self.brother = None

    l = 0

    @classmethod
    def printtree(self):
        if self is not None:
            if self.brother is not None:
                self.brother.printtree()
        for i in range(Tree.l):
            print("    ")
        print("\\__%i\n" % self.data)
        Tree.l += 1
        if self.son is not None:
            self.son.printtree()
        Tree.l -= 1

        if Main == 0:
            print("\nДерево пустое!\n")

    def generation_tree(self):

        r = random.randrange(0, 2)
        if self == Main:
            r = 1
        if r == 1:
            if self.son is None:
                self.son = Tree()
                print("\nson")
            else:
                self.son.generation_tree()
        else:
            if self.brother is None:
                self.brother = Tree()
                print("\nbrother")
            else:
                self.brother.generation_tree()


Main = Tree()
k = 0
n = 0
while 0 <= n <= 10:
    if n == 0:
        print("\nМеню:"
              "\n0. Вывести меню"
              "\n1. Генерация случайного дерева"
              "\n2. Текстовая визуализация дерева"
              "\n3. Создать новый корень"
              "\n4. Создать новый узел типа son"
              "\n5. Создать новый узел типа brother"
              "\n6. Найти родительский узел"
              "\n7. Найти старший братский узел"
              "\n8. Удалить узел"
              "\n9. Удалить дерево"
              "\n10. Определить глубину максимальной вершины дерева (кол-во шагов до нее)\n")

    n = int(input("\nВыберите желаемое действие: n = "))

    if n == 1:
        # k = int(input("\nПожалуйста, введите количество элементов: k = "))
        for x in range(4):
            Main.generation_tree()

    if n == 2:
        Main.printtree()

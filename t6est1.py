class Computer:
    def __init__(self, memory=None, model=None):
        self.memory = memory
        self.model = model

    def __repr__(self):
        return str(self.__dict__)


class PC(Computer):

    def __init__(self, model=None, memory=None,  mouse=None, keyboard=None):
        Computer.__init__(self, memory, model)
        self.mouse = mouse
        self.keyboard = keyboard

a = PC(2000)
print(a)

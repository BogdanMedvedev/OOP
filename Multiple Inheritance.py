# Пример множественного наследования

class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print('Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name},{self.weight},{self.price}')


class MixinLog:
    ID = 0

    def __init__(self):
        super().__init__()
        print('MixinLog')
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_log(self):
        print(f'{self.id}: товар был продан')


class MixinLog2:
    def __init__(self):
        super().__init__()
        print('MixinLog2')

    def print_info(self):
        print('Вызов метода print_info из MixinLog2')


class NoteBook (Goods, MixinLog, MixinLog2):
    def print_info(self):
        MixinLog2.print_info(self)


# Проверка
n = NoteBook('Apple', 1.5, 5000)
n.print_info()
n.save_log()
n.print_info()  #Метод будет вызван из класса MixinLog2, так как в MixinLog2 мы переопределили данный метод
print(NoteBook.__mro__)

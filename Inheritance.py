#Пример реализации наследования

class Geom:
    """"Класс для демонстрации принципа ООП наследования"""

    name = 'Geom'
    def __init__(self,x,y,z,q):
        self.x = x
        self.y = y
        self.z = z
        self.q = q

    def set_coords (self, x ,y, z, q):
        self.x = x
        self.y = y
        self.z = z
        self.q = q

    def get_coords (self):
        return self.x, self.y, self.z, self.q

    def draw(self):
        """Метод базового класса, в дальнейшем будем его переопределять"""
        return 'Метод draw из класса Geom'



class Line (Geom):
    def draw (self):
        """Переопределяем метод из базового класса, возвращаем 'Линия'"""
        return 'Линия'

class Rect (Geom):
    """Здесь, к примеру, нам нужен новый атрибут для данного экземпляра класса."""
    def __init__(self,x,y,z,q,flit = None):
        super().__init__(x,y,z,q)
        self.flit = flit

    def draw (self):
        """Переопределяем метод из базового класса, возвращаем 'Прямоугольник'"""
        return 'Прямоугольник'

l = Line(1,2,3,4)
r = Rect(5,6,7,8,1)
print (l.__dict__)
print (r.__dict__)
print (l.get_coords())
print (r.get_coords())
print (l.draw()) #В каждом экземпляре мы переопределяем данный метод
print (r.draw()) #В каждом экземпляре мы переопределяем данный метод

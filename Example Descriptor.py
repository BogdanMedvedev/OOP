# Сначала создаем класс-дескриптор.
# Мы сможем его использовать в других классах для удобства
# благодаря ему не нужно будет создавать кучу свойств сеттеров и геттеров для каджого объекта.
class Integer:
    """Класс класс-дескриптор"""
    @staticmethod
    def verify_coords(coord):
        if type(coord) != int:
            raise TypeError('Координата должна быть целым числом')

    def __set_name__(self, owner, name):
        self.name = '_'+name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coords(value)
        setattr(instance, self.name, value)


class Pont3D:
    """Класс для того, чтобы показать, как работет дескриптор"""
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, a=1, b=2, c=3):
        self.x = a
        self.y = b
        self.z = c

# Проверка
# a = Pont3D(2,5,6)
# b = Pont3D(1,1,1)
# a.x = 13
# b.x = 14
# print (a.x)
# print (b.x)

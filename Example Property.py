#Пример того, как использовать Property
from string import ascii_letters
from re import findall

class Person:
    """Класс, в котором содержится информация о человеке"""

    RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.__fio = fio.split()
        self.old = old
        self.ps = ps
        self.weight = weight

    #Проверка на валидный возраст
    @staticmethod
    def verify_old(old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError ('Возраст должен быть числом от 14 до 120')

    # Проверка на валидный вес
    @staticmethod
    def verify_weight(weight):
        if type(weight) != float or weight < 20:
            raise TypeError('Вес должен быть вещественным числом от 20 и выше')

    # Проверка на паспорт
    @staticmethod
    def verify_ps(ps):
        if type(ps) != str:
            raise TypeError('Паспорт должен быть строкой')
        if not findall(r'\b\d{4} \d{6}\b',ps):
            raise TypeError('Неверный формат паспорта')

    # Проверка на валидные ФИО
    @classmethod
    def verify_fio (cls, fio):
        letters = cls.RUS + cls.RUS.upper() + ascii_letters
        if type(fio) != str:
            raise TypeError ('ФИО должно быть строкой')
        if len (fio.split()) != 3:
            raise TypeError ('Неверный формат ФИО')

        for i in fio.split():
            if len (i.strip(letters)) != 0:
                raise TypeError ('В ФИО можно исполльзовать только буквенные символы и дефис')

    @property
    def fio (self):
        return self.__fio

    @property
    def old (self):
        return self.__old

    @old.setter
    def old (self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps)
        self.__ps = ps


p = Person('Медведев Богдан Александрович', 14, '4444 607000', 21.0)
print (p.fio)
print (p.ps)









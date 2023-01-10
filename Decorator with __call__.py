from math import sin

# Ниже реализован декаратор на уровне класса с помощью __call__

class Derivate:
    """Простой класс для демонстрации одной из возможностей __call__.
     В данном случае данный класс будет декаратором"""
    def __init__(self, func):
        self.__func = func

    def __call__(self, x, dx=1.5, *args, **kwargs):
        """Прибавляем dx к передаваемому в функцию значению"""
        return self.__func(x+dx)

@Derivate
def df_sin_with_derivate(x):
    return sin(x)

def df_sin(x):
    return sin(x)

# Проверка
print(df_sin_with_derivate(4))
print(df_sin(4))

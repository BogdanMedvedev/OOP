#Благодря call появляется возможность вызывать
# с помощью скобок (как обычные функции) ЭКЗЕМПЛЯРЫ классов

class StripChars:
    def __init__(self, chars = ' '):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Необходимо ввести строку')
        return args[0].strip(self.__chars)

s1 = StripChars(' H!')
a = s1(' HelloWorld! ') #Если бы не __call__, то мы бы не могли так вызвать экземпляр класса
print (a) #Из строки ' HelloWorld! ' будет убран пробел, буква H и восклицательный знак

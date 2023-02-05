"""Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""

lst = []
inp = True


class Check(Exception):
    def __init__(self, inp):
        self.inp = inp

    def valid(self):
        inp_val = inp.isalpha()
        if inp_val:
            raise Check('Wrong data')
        else:
            return 'Integer is Valid'


while True:
    try:
        inp = input('Enter integer or type "stop" for exit: ')
        if inp == 'stop':
            if lst:
                for i in lst:
                    if i:
                        print(f'{i} is integer')
            exit()
        print(Check.valid(inp))
    except Check as err:
        print(err)
        break
    lst.append(inp)
print()
print(f'Listed integers: ')
for i in lst:
    if i:
        print(f'{i} is integer')

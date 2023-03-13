"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class MyExcep(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    a = input('Введите чисело, для завершения введите stop: ')
    if a == 'stop':
        break
    else:
        try:
            if not a.isdigit():
                raise MyExcep('Вы ввели не число!')
        except MyExcep as err:
            print(err)
        else:
            my_list.append(a)

print(my_list)

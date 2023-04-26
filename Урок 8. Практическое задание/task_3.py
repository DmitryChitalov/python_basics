"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    digit = input('Введите целое число или "stop" для окончания ввода: ')
    if digit == 'stop':
        print(my_list)
        break
    try:
        if digit.isdigit():
            my_list.append(int(digit))
        else:
            raise MyError('Ошибка!')
    except MyError as err:
        print(err)

"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class MyException(Exception):
    '''Исключение для проверки чисел'''
    def __init__(self, msg):
        self.msg = msg

values_list = []
PERMITTED_CHARS = '1234567890'

while True:
    try:
        user_val = input('Введите число: ')
        if user_val == '':
            raise MyException("Вы ничего не ввели")
        for char in user_val:
            if char not in PERMITTED_CHARS or char == '':
                raise MyException("Введенное значение не является числом")
        values_list.append(user_val)
    except MyException as err:
        print(err)
        print()
        print('Массив числел:')
        print(values_list)
        break

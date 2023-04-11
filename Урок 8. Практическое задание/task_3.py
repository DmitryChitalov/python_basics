"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class ExampleError(Exception):
    def __init__(self, txt):
        self.txt = txt


user_list = []

for i in range(5):
    user_input = input('Введите число: ')

    try:
        if user_input.isdigit():
            user_list.append(int(user_input))
        else:
            raise ExampleError('Вы ввели не число')
    except ExampleError as err:
        print(err)


print(user_list)


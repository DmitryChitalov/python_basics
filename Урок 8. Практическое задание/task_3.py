"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NumberCheck(Exception):
    def __init__(self, catch_err):
        self.catch_err = catch_err


user_input = []
while True:
    try:
        input_digit = input('Введите число: ')
        if input_digit.isnumeric() == 'pause':
            break
        elif input_digit.isalpha():
            raise NumberCheck('Не является числом, введите число!')
    except NumberCheck as err:
        print(err)
    else:
        user_input.append(int(input_digit))
print(user_input)

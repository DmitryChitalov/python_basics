"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у
пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class Myexcept(Exception):
    def __init__(self, txt):
        self.txt = txt


user_list = []

while True:
    user_input = input('Введите число или "q" >>> ')

    if user_input == 'q':
        break
    try:
        if user_input.isdigit():
            user_list.append(int(user_input))
        elif not user_input.isdigit():
            raise Myexcept(f'Было введено не число - {user_input}')
    except Myexcept as err:
        print(err)

print(user_list)

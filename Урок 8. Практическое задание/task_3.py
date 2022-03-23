"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать
у пользователя данные и заполнять список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class MyError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input('Enter one number '))
                    ex = input(
                        f'You add {user_val} in the list. '
                        f'Continue? y/n: ').lower()
                    self.my_list.append(user_val)
                    if ex == 'n':
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                ex = input(
                    f'You should enter a number.'
                    f' Continue? y/n: ').lower()
                if ex == 'n':
                    print(self.my_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()

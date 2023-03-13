"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class MyError(Exception):
    def __init__(self):
        pass


class ListOfNumbs:
    def __init__(self):
        self.my_list = []

    def input_values(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input('Введите числа по одному: '))
                    nonstop = input(
                        'Для прекращения ввода: "q" Для продолжения: "enter": ')
                    self.my_list.append(user_val)
                    if nonstop == 'q' or nonstop == 'Q':
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                nonstop = input(
                    f"Вы ввели не число! Повторить попытку? Y/n: ")
                if nonstop == 'n' or nonstop == 'N':
                    print(self.my_list)
                    break
                else:
                    self.input_values()


numb_list = ListOfNumbs()
numb_list.input_values()

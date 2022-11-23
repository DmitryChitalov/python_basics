"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


def only_num():
    num_list = []
    while True:
        user_list = input(f'Введите число, или q для выхода: ')
        if user_list == 'q':
            break
        try:
            if not user_list.isnumeric():
                raise NotNumber('Ошибка! Введено не число!')
            num_list.append(user_list)
        except NotNumber as err:
            print(err)
    print(f'------------------------------------------------------ \nВы ввели следующие числа:\n')

    print(*num_list)

only_num()

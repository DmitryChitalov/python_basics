"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class OnlyNumbersError(Exception):
    def __init__(self, txt):
        self.txt = txt


def checking():
    try:
        numbers = input('Введите числа через пробел: ')
        mass_numbers = []
        for i in numbers.split():
            if not i.replace('.', '').isdigit():
                raise OnlyNumbersError('Ошибка! Строка должна содержать только числа!')
            else:
                mass_numbers = [*mass_numbers, int(i)]
        print(mass_numbers)
    except OnlyNumbersError as e:
        print(e)
        checking()


checking()

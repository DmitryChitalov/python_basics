"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NaNError(Exception):
    def __init__(self, txt):
        self.txt = txt


def number_filter(string):
    if string.isdigit():
        return string
    else:
        try:
            float(string)
            return string
        except ValueError:
            raise NaNError(f'Ошибка: {string} - не число')


input_txt = ''
counter = 1
numbers_list = []
print("Введите числа по одному, для выхода введите 'stop'")
while input_txt != 'stop':
    try:
        input_txt = input(f'{counter}: ')
        numbers_list.append(number_filter(input_txt))
        counter += 1
    except NaNError as e:
        if input_txt != 'stop':
            print(e.txt)

print(f'Результат:\n{numbers_list}')

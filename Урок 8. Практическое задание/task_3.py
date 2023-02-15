"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class ControlType(Exception):
    pass


my_list = []
while True:
    try:
        value = input('Введите число в список или введите "q" для завершения программы:')
        if value == 'q' or value == 'Q':
            break
        if not value.isdigit():
            raise ControlType(value)
        my_list.append(int(value))
    except ControlType as ex:
        print(f'{ex} - не число!')
print(my_list)

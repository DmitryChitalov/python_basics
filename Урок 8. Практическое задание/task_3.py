"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class ListValuesCheckUp(Exception):
    text = 'Задайте значения списка числами'

    def __str__(self):
        return self.text


try:
    input_cnt = 5
    test_lst = []
    print(f'Задайте числами значения списка:')
    for i in range(0, input_cnt):
        value = input(f'Значение {i}/{input_cnt}: ')
        if not value.isdigit():
            raise ListValuesCheckUp
        test_lst.append(float(value))
        i = i + 1
except ListValuesCheckUp:
    print(ListValuesCheckUp.text)
finally:
    print(f'Список введённых значений:\n{test_lst}')






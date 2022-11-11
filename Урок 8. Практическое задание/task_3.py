"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class OwnError(Exception):
    def __init__(self, c_data, el):
        self.c_data = c_data
        self.num = el + 1
        print(
            f'Элемент ввода не прошел проверку, номер в последовательности {self.num} значение {c_data} тип'
            f' элемента: {type(c_data)}')


inp_data = input("Введите последовательность чисел:")
res_string = inp_data.split()
print(f' Вы ввели: {res_string}')
el = 0
int_list = []
for x in res_string:
    c_data = res_string[el]
    if res_string[el].isdigit():
        int_list.append(res_string[el])
    else:
        # создать объект класса исключения с выводом соотв. сообщения в методе
        OwnError(c_data, el)
    el += 1
print(f'Итоговая последовательность: {int_list}')

"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class ListNumCheck(Exception):

    def __init__(self, in_el):
        self.txt = f"Вы ввели данные, отличные от чисел. Значение {in_el} проигнорировано."

    def __str__(self):
        return self.txt


inp_data = input("Введите числа в одну строку через пробел: ")
tmp_list = inp_data.split(" ")
res_list = []
for el in tmp_list:
    try:
        if not el.isdigit():
            raise ListNumCheck(el)
    except ListNumCheck as err:
        print(err)
    else:
        res_list.append(int(el))
print(res_list)

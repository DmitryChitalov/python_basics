"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class OnlyIntList(Exception):
    def __str__(self):
        return f"Элемент не integer, удаляется ..."


try:
    clean_list = []
    is_there = False
    list_tmp = input("Введите элементы списка через пробел: ").split()
    for item in list_tmp:
        if item not in map(str, range(0, 10)):
            is_there = True

        else:
            clean_list.append(int(item))
    if is_there:
        raise OnlyIntList

except OnlyIntList as err:
    print(err)

print(clean_list)

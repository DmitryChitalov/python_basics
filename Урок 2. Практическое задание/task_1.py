"""
Задание 1. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""

my_list = [10, None, -30, 'True', True, 9.5]


def my_type(element):
    """

    :param element:
    :return:
    """
    for element in range(len(my_list)):
        print(type(my_list[element]))
    return


my_type(my_list)

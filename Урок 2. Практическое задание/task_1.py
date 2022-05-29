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

new_l = ['стул', 'нога', 25, -25, None]
print(type(new_l))


def my_type(el):
    for el in range(len(new_l)):
        print(type(new_l[el]))
    return


my_type(new_l)

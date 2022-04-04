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

my_list = ['Text', 39, 39.9, True, None, ['Obi', 'Yoda', 'Wader'], {'Hulk', 'Stark', 'Tor'}, ('BlackWidow', 'HawkEye')]
for my_list in my_list:
    print(f'{my_list} - {type(my_list)}')
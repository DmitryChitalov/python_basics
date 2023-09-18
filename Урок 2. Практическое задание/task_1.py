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

my_list = [17, 'september', 1986, 2.5, ['12345'], (tuple('abcdefg')), (dict(key_1='cat', key_2='кошка')), True, None]
for el in my_list:
    print(type(el))  # Вывести тип данных каждого элемента из списка my_list

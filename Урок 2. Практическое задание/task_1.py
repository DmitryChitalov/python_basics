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

lst_1 = [5, "string", 0.15, True, None]
for el in lst_1:
    print(type(el))


lst_1 = [5, "string", 0.15, True, None]
for i in range(len(lst_1)):
    print(type(lst_1[i]))


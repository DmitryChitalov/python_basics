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
ls = [5, "string", 0.15, True, None]
for val in ls:
    print(type(val))

print(type(ls[0]) is int)
print(type(ls[1]) is str)
print(type(ls[2]) is float)
print(type(ls[3]) is bool)
print(ls[4] is None)


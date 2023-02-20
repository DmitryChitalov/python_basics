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
my_list = ['greek', 42, 0.5, False, ('cake is a lie', True, 23), {
    1, 2, 3, 45, '28'}]
print(f'the current list is {my_list}')
print('every element type is:')
for el in my_list:
    print(type(el))

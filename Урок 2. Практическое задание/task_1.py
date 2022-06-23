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

int_var = 1
float_var = 1.11
str_var = "My string"
list_var = ['list', '1']
dict_var = {'name': 'Artem', 'age': '26'}
tuple_var = ('tuple', '2')
bool_var = True
none_var = None
check_list = [int_var, float_var, str_var, list_var, tuple_var, dict_var, bool_var, none_var]

for i in check_list:
    print(f'Тип данных {i} - {type(i)}')
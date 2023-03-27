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
my_list = [{"set1": "Moscow", "set2": "Berlin"}, {"yellow", "green", "blue"}, None, -30, 'Phone', True, 10.2 , ['1' , '2']]

def my_type(element):
    for element in my_list:
        print(type(element))

my_type(my_list)
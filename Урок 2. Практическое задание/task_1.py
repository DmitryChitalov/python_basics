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

any_types = ["abc", 34, True, 0.12367, None, [1, 2, 3], ('a', 'b', 'c'),
             {11, 3, 8, 4}, {"key1": "val1", "key2": "val2"}, b'bytes']

for el in any_types:
    print(type(el))

print("---------------------------------")

for el in any_types:
    print(f"element '{el}' of type {type(el)}")

print("---------------------------------")

list_of_string = list('simple string')
print(list_of_string)

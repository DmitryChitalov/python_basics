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

some_list = [1, 2, 3.14, "PI", False, "SomeString", True, "True", None]
print(f"List: {some_list}")

for element in some_list:
    print(f"The value: '{element}' is of '{type(element).__name__}' type")

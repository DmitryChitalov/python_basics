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

my_test_list = [
    5,
    "string",
    0.15,
    True,
    None,
    complex(5,6),
    [],
    (),
    {},
    set(),
    b'text',
    bytearray(b"some text")]

print(f"Для писка {my_test_list}")
print("результат\n")

for el in my_test_list:
    print(type(el))

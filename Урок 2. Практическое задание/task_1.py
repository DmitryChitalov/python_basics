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

my_list = [5, "string", 0.15, True, None]
print(type(my_list[0]))
print(type(my_list[2]))
print(type(my_list[3]))
print(type(my_list[4]))
print(list(map(type, my_list)))
"""
my_list = [5, "string", 0.15, True, None]
len_my_list = len(my_list)
i = 0
while i < len_my_list:
    print(type(my_list[i]))
    i += 1

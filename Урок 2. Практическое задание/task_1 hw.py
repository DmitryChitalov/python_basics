__author__ = 'AndreiM'
__version__ = "1.2 26.03.2023"
print("\n task_1 \n -------- \n")

my_list = [5, "String", 0.15, True, None]
print(my_list[:])

for i in range(len(my_list)):
    print(type(my_list[i]))

""""
Задание 1. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""
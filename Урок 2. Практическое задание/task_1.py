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
NUMBER = 10
<<<<<<< HEAD
lista = (b"NAme", NUMBER, 3.1, "age", "Jone")
for lists in lista:
=======
list_1 = [b"NAme", NUMBER, 3.1, "age", "Jone"]
for lists in list_1:
>>>>>>> Amendments_Homework#1,2,3
    print(type(lists))

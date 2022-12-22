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
dif_list = [8, 6.5, True, [7,4], "hellow", {"team": "Arsenal", "coach": "Mikel Arteta Amatriaín"}, (5,6)]
for i in range (len(dif_list)) :
    print(f"Тип переменной: {type(dif_list[i])}")

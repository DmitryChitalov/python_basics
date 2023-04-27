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
my_l = []  # создание пустого списка

# заполнение списка различными типами данных
my_l.append(5)
my_l.append(5.10)
my_l.append('string')
my_l.append([5, 5.10, 'string'])
my_l.append({1, 5, 6, 7, 9, 10, 4})
my_l.append(frozenset([1, 3, 3, 5, 8, 5, 4]))
my_l.append(complex(3, -2))
my_l.append(None)
my_l.append(True)
my_l.append(b'Byte text')
my_l.append(bytearray(b'Byte text'))

# вывод типа данных для каждого элемента списка
for i in my_l:
    print(i, type(i))

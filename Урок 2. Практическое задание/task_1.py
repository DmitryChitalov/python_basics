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
l = []  # создадим пустой список

# заполним список элементами различных типов данных
l.append(5)
l.append(5.15)
l.append('string')
l.append([5, 5.15, 'string'])
l.append({'integral': 5, 'float': 5.15, 'string': 'string'})
l.append((5, 5.15, 'string'))
l.append({1, 2, 2, 2, 6, 5, 6})
l.append(frozenset([1, 2, 2, 2, 6, 5, 6]))
l.append(complex(5, -3))
l.append(None)
l.append(True)
l.append(b'Byte text')
l.append(bytearray(b'Byte text'))

# Используем функцию type() для проверки типа
for i in l:
    print(i, type(i))

"""
Задание 3.

Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N.

Решение:
"""

n = int(input('Введите число N : '))
integer_degrees = ''
for i in range(0, n):
    if 2 ** i <= n:
        integer_degrees += f'{2 ** i} '
print(f'Целые степени двойки : {integer_degrees}')
"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
pos_int = input('Введите число n:  ')
result = int(pos_int) + int(pos_int * 2) + int(pos_int * 3)
print(f'n + nn + nnn = {result}')


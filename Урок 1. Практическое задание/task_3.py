"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input('Введите число n: '))
summ = n + n ** 2 + n ** 3
print(f'n + nn + nnn = {summ}')
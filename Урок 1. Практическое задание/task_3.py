"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = input('Введите число n: ')
sum_n = int(n) + int(n + n) + int(n + n + n)
print(sum_n)

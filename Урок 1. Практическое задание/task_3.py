"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = input('Введите целое положительное число n ')
first = int(n)
second = int(2 * n)
third = int(3 * n)

print(first + second + third)

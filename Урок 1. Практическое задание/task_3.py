"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = input('Введите число n: ')
nn = n + n
nnn = n + n + n
total = int(n) + int(nn) + int(nnn)
print(f"n + nn + nnn = {total}")

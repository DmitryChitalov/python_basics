"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input('Введите число n:'))
n_str = str(n)
nn = n_str + n_str
nnn = n_str + n_str + n_str
print(f'n + nn + nnn = {n + int(nn) + int(nnn)}')


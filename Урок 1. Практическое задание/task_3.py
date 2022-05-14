"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input('Введите число n: '))
nn = n + n
nnn = n + n + n
conc = str(n) + str(nn) + str(nnn)
print(f'n + nn + nnn = {conc}')

"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = int(input('Введите число n: '))
str_n = str(n)
nn = str_n + str_n
nnn = str_n + str_n + str_n
amount = n + int(nn) + int(nnn)
print(f'{n} + {nn} + {nnn} = {amount}')


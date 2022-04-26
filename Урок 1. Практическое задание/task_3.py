"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
digit = int(input("Type your N digit:"))
solu = digit + digit * 11 + digit * 111
print(f'n + nn + nnn = {solu}')

"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
user_numbers = int(input('Введите целое положительное число: '))
Calculation = user_numbers + user_numbers * 11 + user_numbers * 111
print(f' n+nn+nnn= {Calculation}')
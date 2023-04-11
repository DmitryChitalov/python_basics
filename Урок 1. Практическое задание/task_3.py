"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
term_1 = input('Введите целое положительное число n: ')
term_2 = term_1 + term_1
term_3 = term_1 + term_1 + term_1
print(f'n + nn + nnn = {int(term_1) + int(term_2) + int(term_3)}')

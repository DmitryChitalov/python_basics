"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
num = input('Введите число n: \n')
while not (num.isdigit() and len(num) == 1):
    num = input('У вас не вышло. Введите цифру: \n')
print(f'n + nn + nnn = {int(num) + int(num * 2) + int(num * 3)}')

"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

user_num = input('Введите число n: ')

user_num_1x = int(user_num)
user_num_2x = int(user_num + user_num)
user_num_3x = int(user_num + user_num + user_num)

summ = user_num_1x + user_num_2x + user_num_3x

print(f'n + nn + nnn = {summ}')

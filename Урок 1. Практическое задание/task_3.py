"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

var_user_number = int(input('Введите число n: '))
var_second_number = int(f'{var_user_number}{var_user_number}')
var_third_number = int(f'{var_user_number}{var_second_number}')
var_sum_all_number = var_user_number + var_second_number + var_third_number

print(f'{var_user_number} + {var_second_number} + {var_third_number} = {var_sum_all_number}')


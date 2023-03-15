"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

user_num = (input('Введите целое положительное число: '))
user_num_int = int(user_num)

max_number = 0
while user_num_int != 0:
    max_number = max(max_number, user_num_int % 10)
    user_num_int //= 10

print(f'Самая большая цифра в числе: {max_number}')

# Вариант решения №2
# while user_num_int != 0:
#     rest = user_num_int % 10
#     if max_number < rest:
#         max_number = rest
#     user_num_int //= 10
#

# Вариант решения №3
#number_list = list(user_num)
#max_number = 0
# for i in number_list:
#     num = int(i)
#
#     if max_number < num:
#         max_number = num



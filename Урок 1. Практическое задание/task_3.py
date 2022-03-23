"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

input_number = input('Enter any number ')
number_1 = int(input_number + input_number)
number_2 = int(input_number + input_number + input_number)
print(int(input_number) + number_1 + number_2)

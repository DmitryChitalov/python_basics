"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

str_number = input("Введите число n: ")
result = int(str_number) + int(str_number + str_number) + \
    int(str_number + str_number + str_number)

print(f"n + nn + nnn = {result}")

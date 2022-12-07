"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""


number_user = input("Введите число n: ")
print(f"n + nn + nnn = {int(number_user) + int(number_user * 2) + int(number_user * 3)}")

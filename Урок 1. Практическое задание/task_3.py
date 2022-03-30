"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
user_number = str(input('Введите целое положительное число - '))
print(int(user_number) + int(str(user_number + user_number)) + int(str(user_number + user_number + user_number)))
"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = input("Введите число n: ")

number = int(n)
double_number = int(n+n)
triple_number = int(n+n+n)

print(number + double_number + triple_number)
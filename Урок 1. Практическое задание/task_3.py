"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input("Введите целое, положительное число n: "))
print(f"n + nn + nnn = {n}{n + n}{n + n + n}")

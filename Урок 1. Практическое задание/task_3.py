"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = int(input("Введите число от 0 до 9: "))
result = n + n * 11 + n * 111
print(f"n + nn + nnn = {result}")
"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
number = input("Введите число n: ")
n = number
nn = n + n
nnn = n + nn
print(f"n + nn + nnn = {int(n) + int(nn) + int(nnn)}")

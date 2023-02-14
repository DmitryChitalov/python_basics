"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = input("Введите целое, положительное число:")
# i = 0
# t = ''
# number = 0
# while i < int(n):
#     t = t + n
#     number = number + int(t)
#     i = i + 1
# print(number)

summa = int(n) + int(2*n) + int(3*n)
print(f"n + nn + nnn = {summa}")
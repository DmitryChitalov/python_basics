"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

answer = (input("Введите целое положительное число n "))
a = answer
b = answer+answer
c = b + answer
d = int(a) + int(b) + int(c)
print(d)

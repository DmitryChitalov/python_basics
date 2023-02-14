"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = int(input("Введите число n: "))
sum_n = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print("n + nn + nnn =", sum_n)

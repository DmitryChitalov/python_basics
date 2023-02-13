"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = input("Введите положительное целое число n: ")
nn = int(str(n) + str(n))
nnn = int(str(n) + str(n) + str(n))
sum = int(n) + nn + nnn
print("n + nn + nnn =", sum)

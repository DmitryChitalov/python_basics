"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

count = input("Введите число n:")
summ = int(count) + int(2 * count) + int(3 * count)
print(summ)
"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

number = int(input("Введите число n "))
print("n + nn + nnn = " + str(number) + str(number + number) + str(number + number + number))

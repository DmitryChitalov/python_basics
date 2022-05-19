"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

number = input("Введите число: ")
a = int(number + number)
b = int(number+number+number)
sum = int(number) + a + b
print(sum)

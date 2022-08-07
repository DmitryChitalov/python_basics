"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""


number = int(input("Введите целое число n: "))
a = str(number)
b = a + a
c = a + b
print("n + nn + nnn = ", number + int(b) + int(c))

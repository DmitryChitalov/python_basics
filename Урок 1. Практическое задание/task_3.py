"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
digit = int(input("Input number n: "))
x = str(digit)
x1 = x + x
x2 = x + x + x
result = digit + int(x1) + int(x2)
print("Print: ", result)
Пример:
Введите число n: 3
n + nn + nnn = 369
"""

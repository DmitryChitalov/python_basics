"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = int(input("Input number from 1 to 9: n = "))

if n > 9 or n < 1:
    print("Inputted number is out of predefined range")  # проверка на вхождение в область допустимых значений
else:
    m = n * 10 + n
    k = n * 100 + m
    print("Result: n + nn + nnn = ", n + m + k)

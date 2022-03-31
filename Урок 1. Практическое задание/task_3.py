"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

number = int(input("Введите число: "))

s = str(number)

number2 = s + s
number3 = s + s + s

sum0 = number + int(number2) + int(number3)

print(f"Сумма чисел: ", sum0)

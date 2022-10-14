"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

digit = input("Введите любое число: ")
print(
    f"{digit} + {digit + digit} + {digit + digit + digit} = "
    f"{int(digit) + int(digit + digit) + int(digit + digit + digit)}")

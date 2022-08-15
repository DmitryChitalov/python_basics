"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
u_number = int(input("Введите целое положительное число:"))
# a = u_number + 2 * u_number + 3 * u_number
# a = u_number + 5 * u_number
a = 6 * u_number
print(f"n + nn + nnn = {a}")

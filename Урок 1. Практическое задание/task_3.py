"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

"""ФИО Суслин Александр"""

value = input("Enter integer (n): ")

result = int(value) + int(value + value) + int(value + value + value)

print(f"Template (n + nn + nnn) result: {result}")

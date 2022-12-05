"""
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
Пример:
Введите число n: 3
n + nn + nnn = 369
"""

integer_from_user = input("Введите целое число: ")

print(f"Странное упражнение, в формате (n + nn + nnn), имеет следующее решение: \
{int(integer_from_user) + int(integer_from_user * 2) + int(integer_from_user * 3)}")


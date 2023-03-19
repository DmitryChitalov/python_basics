"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
namber = int(input("ведите целое положительное число: "))
namber1 = str(namber)
a1 = namber1 + namber1
a2 = namber1 + namber1 + namber1
a3 = namber + int(a1) + int(a2)
print("ответ:", a3)

"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input("Введите число n: "))
m1 = str(n)
m2 = m1 + m1
m3 = m1 + m1 + m1
summ = n + int(m2) + int(m3)
print("Сумма n + nn + nnn =", summ)
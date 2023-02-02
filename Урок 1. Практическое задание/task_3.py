"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input("Введите число n "))
change = str(n)
c1 = change + change
c2 = change + change + change
total = n+int(c1)+int(c2)
print(f"n + nn + nnn = {total}")
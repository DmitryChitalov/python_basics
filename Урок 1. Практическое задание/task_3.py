"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input("Введите число n: "))
comp = str(n) + str(n * 2) + str(n * 3)
print(f'n + nn + nnn = {comp}')  # var1
print(f"n + nn + nnn = {n+(n*11)+(n*111)}")  # var2
print(f"n + nn + nnn = {n*(1+11+111)}")  # var3
print(f"n + nn + nnn = {str(n) + str(n * 2) + str(n * 3)}")  # var4

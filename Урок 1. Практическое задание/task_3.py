"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input("Введите число"))
x = str(n)
nn = x + x
nnn = nn + x
print(n, nn, nnn)
print(f"n + nn + nnn = ", n + int(nn) + int(nnn))

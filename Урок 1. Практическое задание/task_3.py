"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input("Введите число n: "))
d1 = str(n)
d2 = d1 + d1
d3 = d1 + d1 + d1
comp = n + int(d2) + int(d3)
print(f"n + nn + nnn = {comp}")
print(f"{d1} + {d2} + {d3} = {comp}")  # test

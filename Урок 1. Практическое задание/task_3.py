"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
count = input("Введите число n: ")
count_1 = int(count)
str_2 = count + count
count_2 = int(str_2)
str_3 = count + count + count
count_3 = int(str_3)
res = count_1 + count_2 + count_3
print(f"n + nn + nnn = {res}")

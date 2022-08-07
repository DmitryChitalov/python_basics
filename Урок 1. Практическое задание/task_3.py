"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n_srting = input("Введите целое положительное число: ")
number_1 = n_srting * 2
number_2 = n_srting * 3
total_sum = int(n_srting) + int(number_1) + int(number_2)
print(f"n + nn + nnn = {total_sum}")
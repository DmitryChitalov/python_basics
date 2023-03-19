"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
num_plus = input("введите целое положительное число ")
sum = int(num_plus) + int(num_plus + num_plus) + int(num_plus + num_plus + num_plus)
print(f"сумма равна {sum}")

"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input("Введите целое положительное число: "))
n_string = str(n)
print(f"{n_string}+{2 * n_string}+{3 * n_string}={n + int(2 * n_string) + int(3 * n_string)}")


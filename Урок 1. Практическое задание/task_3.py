"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = str(input("Введите число: "))
one_n = n
two_n = f"{n}{n}"
three_n = f"{n}{n}{n}"
result = f"{one_n}+{two_n}+{three_n} = {int(one_n) + int(two_n) + int(three_n)}"
print(result)

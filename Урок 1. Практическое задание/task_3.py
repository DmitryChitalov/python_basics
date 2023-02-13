"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

numb_1 = input("Введите число n: ")
numb_2 = numb_1 + numb_1
numb_3 = numb_1 + numb_1 + numb_1
my_sum = int(numb_1) + int(numb_2) + int(numb_3)
print(f"Сумма чисел n + nn + nnn = {numb_1} + {numb_2} + {numb_3} = {my_sum}")

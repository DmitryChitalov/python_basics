"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
digit = int(input("введите целое положительное число: "))
print(f'{digit}{2 * digit}{3 * digit}')
# print(str(digit) + str(2*digit) + str(3*digit))

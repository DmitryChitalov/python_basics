"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
chisl = input('Введите целое положительное число: ')
sum = int(chisl) + int(chisl+chisl) + int(chisl+chisl+chisl)
print(sum)

"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
numb = int(input('Введите число от 0 до 9: '))
print(numb + numb*11 + numb*111)

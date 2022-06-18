"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = int(input('Введите число n: '))
temp = str(n)
nn = temp + temp
nnn = temp + temp + temp
summ = n + int(nn) + int(nnn)
print('n + nn + nnn =', summ)

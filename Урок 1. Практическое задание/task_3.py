"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = input('Введите число n: ')
temp = n
nn = temp + temp
nnn = temp + temp + temp
summ = int(n) + int(nn) + int(nnn)
print(f'{n} + {nn} + {nnn} =', summ)

"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

num = int(input("Теперь введите любое число, а я предоставлю сумму его ввиде n+nn+nnn:"))
numstr = str(num)
nn = numstr + numstr
nnn = numstr + numstr + numstr
summ = num + int(nn) + int(nnn)
print(f"{num}+{nn}+{nnn}={summ}, как-то так. Давайте дальше?")
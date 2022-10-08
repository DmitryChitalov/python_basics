"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input('Введите число>>>'))
numb = str(n)
n1 = numb + numb
n2 = numb + numb + numb
result = n + int(n1) + int(n2)
print("Результат:", result )

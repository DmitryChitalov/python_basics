"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n=int(input())
print(f'{str(n)}+{2*str(n)}+{3*str(n)}={n}{2*n}{3*n}')
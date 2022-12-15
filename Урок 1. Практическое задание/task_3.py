"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

n = input('Введите число: ')
nn = int(n+n)
nnn = int(n+n+n)
n = int(n)
res = n+nn+nnn
print(res)

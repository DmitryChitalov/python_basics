"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
#Вариант1
n = int(input("Введите число n:"))
res = n + n*11 + n*111
print(f"n+nn+nnn={res}")


#Вариант2
n = input("Введите целое число n:")
res = int(n)+int(n*2)+int(n*3)
print = (f'{n}+{n*2}+{n*3}={res}')

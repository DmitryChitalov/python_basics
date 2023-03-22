"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input("Введите число : "))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
summ = n + int(t1) + int(t2)
print(summ)

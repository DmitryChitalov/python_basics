"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input("Введите целое положительное число: "))
print(str(abs(n)) + str(abs(n * 2)) + str(abs(n * 3)))
""" 
Способ без проверки на то, что вводит юзер, но с защитой от отрицательных чисел
abs можно было сделать перед print, но я решил сделать меньше строк для 
лаконичности.
"""
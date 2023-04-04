"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input("Enter a positive integer  "))
newn = str(n)
n1 = newn + newn
n2 = newn + newn + newn
resultn = n + int(n1) + int(n2)
print(f"Your number is {resultn}")

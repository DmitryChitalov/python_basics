"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = input("Please enter number (n): ")
n1 = int(n)
n2 = int(n + n)
n3 = int(n + n + n)
# print("You first number: ", n1)
# print("You second number: ", n2)
# print("You third number: ", n3)
print("You result n+nn+nnn: ", n1 + n2 + n3)
"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

"""

n = int(input('Введите целое число: '))
sum = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print(f"Сумма n + nn + nn = {sum}")

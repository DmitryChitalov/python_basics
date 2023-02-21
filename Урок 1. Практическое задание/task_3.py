"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
number = int(input("Ввидите целое положительное число n: "))
var = int(number) + int(number * 2) + int(number * 3)
print(f'{number} + {number * 2} + {number * 3} = {var}')

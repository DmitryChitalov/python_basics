"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
number = int(input("Введите первое целое число! "))
sum: int = (number + int(str(number) + str(number)) + int(str(number) + str(number) + str(number)))
print("Сумма чисел n + nn + nnn - %d" % sum)
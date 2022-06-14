"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
number = input("Enter some number: ")
summ = 0
for i in range(1, 4):
    summ += int(number * i)

print("Result is: ", summ)

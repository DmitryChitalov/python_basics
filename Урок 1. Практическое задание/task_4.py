"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""
n = int(input("Введите целое положительное число: "))
maximum_number = 0
while n > 0:
    comparable = n % 10
    if comparable > maximum_number:
        maximum_number = comparable
    n = n // 10

print(maximum_number)

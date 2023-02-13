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

number = int(input("Введите целое положительное число: "))
highest = 0

while number > 10:
    digit = number % 10
    number //= 10
    if digit > highest:
        highest = digit

print(f"Самая большая цифра в числе: {highest}")

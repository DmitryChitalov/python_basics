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

number = input("Введите целое положительное число: ")

highest = "0"

for i in number:
    if i > highest:
        highest = i

print(f"Самая большая цифра в числе: {int(highest)}")
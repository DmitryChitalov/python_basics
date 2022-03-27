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

"""ФИО Суслин Александр"""

value = int(input("Enter integer: "))

max_number = 0

while 0 != value:
    number = value % 10
    if number > max_number:
        max_number = number;

    value = value // 10


print(f"Max number is: {max_number}")

"""value = input("Enter integer: ")

count = 0
max_number = 0

while count < len(value):
    if max_number < int(value[count]):
        max_number = int(value[count])
    count += 1

print(f"Max number is: {max_number}")"""

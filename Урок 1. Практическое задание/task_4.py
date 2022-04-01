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

input_value = input("Please, input a integer value n=")
if str.isdigit(input_value):
    int_value = int(input_value)
    max_number = 0
    division_int = int_value
    while division_int != 0:
        division_remainder = division_int % 10
        division_int = division_int // 10
        if max_number < division_remainder:
            max_number = division_remainder
    print(f"Max char is {max_number}")
else:
    print("Error: your value is not a integer number")
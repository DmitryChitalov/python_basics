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

enter_number = int(input("Ведите целое положительное число: "))
if enter_number > 0:
    max_digit = 0
    current_value = enter_number

    while current_value > 0:
        next_value = current_value // 10
        if next_value > 0:
            last_digit = current_value % (next_value * 10)
        else:
            last_digit = current_value
        current_value = next_value
        if last_digit > max_digit:
            max_digit = last_digit
        if max_digit == 9:
            break
    print(f"Самая большая цифра в числе: {max_digit}")
else:
    print(f"Введенное число должно быть положительным")

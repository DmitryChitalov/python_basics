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

user_input = abs(int(input("Введите целое положительное число ")))
max_from_input = user_input % 10
while user_input >= 1:
    user_input = user_input // 10
    if user_input % 10 > max_from_input:
        max_from_input = user_input % 10
    if user_input > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max_from_input)
        break
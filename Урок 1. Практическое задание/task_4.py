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
user_input = int(input("Please enter a number:"))
largest_number = 0

while user_input > 0:
    current_figure = user_input % 10
    if current_figure > largest_number:
        largest_number = current_figure
    user_input = user_input // 10
    continue

print(largest_number)
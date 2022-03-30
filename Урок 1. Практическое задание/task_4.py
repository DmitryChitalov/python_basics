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

user_number = int(input('Введите целое положительное число: '))
max_number = user_number % 10

while user_number >= 1:
    user_number = user_number // 10
    if user_number % 10 > max_number:
        max_number = user_number % 10
    if user_number > 9:
        continue
    else:
        print('Максимальное число - ', max_number)
        break

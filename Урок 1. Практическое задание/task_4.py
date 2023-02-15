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
var_user_number = int(input('Ведите целое положительное число: '))
var_max_number_in_user_number = 0

while var_user_number > 10:
    last_number_in_user_number = var_user_number % 10
    var_user_number //= 10
    if last_number_in_user_number > var_max_number_in_user_number:
        var_max_number_in_user_number = last_number_in_user_number

print(f'Самая большая цифра в числе: {var_max_number_in_user_number}')

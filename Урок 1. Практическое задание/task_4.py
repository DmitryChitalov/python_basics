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
usr_numb = int(input('Ведите любое целое положительное число: \n'))
if 0 <= usr_numb < 10:
    print(usr_numb)
else:
    mx_digit = 1
    while usr_numb > 10:
        digit = usr_numb % 10
        usr_numb //= 10
        if digit >= mx_digit:
            mx_digit = digit
    print('Самая большая цифра в числе:', mx_digit)

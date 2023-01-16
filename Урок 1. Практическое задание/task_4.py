"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Введите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""


def less4():
    source_digit = int(input('Введите число:'))
    largest_digit = source_digit % 10
    while(source_digit > 9):
        if source_digit % 10 > largest_digit:
            largest_digit = source_digit % 10
        source_digit = source_digit // 10
    print(f'Самая большая цифра в числе: {largest_digit}')


if __name__ == '__main__':
    less4()


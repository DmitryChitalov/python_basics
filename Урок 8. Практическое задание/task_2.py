"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления
на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, text):
        self.text = text


def division_numbers():
    try:
        first_number = int(input('Enter first number '))
        second_number = int(input('Enter second number '))
        if second_number == 0:
            raise OwnError("You can't divide by zero")
        else:
            division_result = first_number / second_number
            return division_result
    except ValueError:
        return 'Ypu should enter a number'
    except OwnError as zero_error:
        return zero_error


print(division_numbers())

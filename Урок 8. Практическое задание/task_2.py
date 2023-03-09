"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class DivisionByZeroError(Exception):
    def __init__(self, message):
        self.message = message

try:
    dividend = int(input('Введите делимое: '))
    divider = int(input('Введите делитель: '))
    if divider == 0:
        raise DivisionByZeroError('Деление на 0 невозможно!')
    else:
        print(dividend / divider)
except ValueError:
    print('Не число!')
except DivisionByZeroError as e:
    print(e)
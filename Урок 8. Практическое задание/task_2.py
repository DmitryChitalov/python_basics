"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        user_divisible = int(input('Введите делимое: '))
        user_divider = int(input('Введите делитель: '))
        if user_divider == 0:
            raise OwnError("Делить на ноль нельзя!")
        else:
            res = user_divisible / user_divider
            return f'{res:.2f}'
    except ValueError:
        return "Вы ввели не число"
    except OwnError as err:
        return err


print(div())

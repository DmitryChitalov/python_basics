"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class MyError(Exception):
    def __init__(self, message):
        self.message = message


def usr_div():
    try:
        numb_1 = int(input('Какое число будем делить: '))
        numb_2 = int(input('На что будем делить: '))
        if numb_2 == 0:
            raise MyError("Делить на ноль нельзя!")
        else:
            res = numb_1 / numb_2
            return f'Результат деления: {res}'
    except ValueError:
        return "Мы работаем только с числами. Пожалуйста, проверьте ввод!"
    except MyError as error:
        return error

print(usr_div())

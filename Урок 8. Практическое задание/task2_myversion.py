"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых
пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        number_1 = int(input('Введите делимое: '))
        number_2 = int(input('Введите делитель: '))
        if number_2 == 0:
            raise Error("Делить на ноль нельзя!")
        else:
            res = number_1 / number_2
            return res
    except ValueError:
        return "Вы ввели не число"
    except Error as err:
        return err


print(div())

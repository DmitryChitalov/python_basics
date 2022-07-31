"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class Divisionbyzero(Exception):
    def __init__(self, txt):
        self.txt = txt


def divide_by_zero(numb_1, numb_2):
    try:
        if numb_2 == 0:
            raise Divisionbyzero("Делить на ноль нельзя")
        print(numb_1 / numb_2)
    except Divisionbyzero as zero_error:
        print(zero_error)


divide_by_zero(5, 0)

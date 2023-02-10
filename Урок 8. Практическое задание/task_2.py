"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ChekDevision(Exception):

    @staticmethod
    def DevisionByZero():
        inp_a = int(input("Введите число а: "))
        inp_b = int(input("Введите число b: "))
        try:
            if inp_b == 0:
                raise ChekDevision
            print(f"{inp_a} / {inp_b} = {inp_a / inp_b}")
        except ChekDevision as err:
            print("На ноль делить нельзя!!")
ChekDevision.DevisionByZero()
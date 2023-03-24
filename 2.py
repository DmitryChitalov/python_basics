"""
Задание 2.
Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByNull(Exception):
    def __init__(self, message):
        self.txt = message


class Calc:
    @staticmethod
    def divide(num, des):
        if des == 0:
            raise DivisionByNull("На ноль делить нельзя!")
        return num / des


if __name__ == '__main__':
    calculator = Calc()

    try:
        number = float(input("Введите число: "))
        desired = float(input("Введите делитель: "))
        result = calculator.divide(number, desired)
        print("Результат:", result)
    except DivisionByNull as exception:
        print(exception)

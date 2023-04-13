"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class CustomZeroDividingError(Exception):
    pass


def divide(number1, number2):
    if number2 == 0:
        raise CustomZeroDividingError()
    return number1 / number2


try:
    num1 = int(input('Input number #1:'))
    num2 = int(input('Input number #2:'))
    print(f"Result: {divide(num1, num2)}")
except CustomZeroDividingError:
    print("Can't divide on zero")
except ValueError:
    print('Incorrect input')

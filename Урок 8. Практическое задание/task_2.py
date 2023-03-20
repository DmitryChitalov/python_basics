"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class DivisionByZeroError(Exception):
    pass

def divide(a, b):
    if b == 0:
        raise DivisionByZeroError("Division by zero is not allowed")
    return a / b

try:
    a = float(input("Enter the dividend: "))
    b = float(input("Enter the divisor: "))
    result = divide(a, b)
    print(f"{a} divided by {b} is {result}")
except ValueError:
    print("Invalid input")
except DivisionByZeroError as e:
    print(e)

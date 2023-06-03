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
        raise DivisionByZeroError("Делить на ноль нельзя")
    return a / b

try:
    a = float(input("Введите число для деления: "))
    b = float(input("Введите число, на которое нужно поделить: "))
    result = divide(a, b)
    print(f"Результат: {result}")
except DivisionByZeroError as e:
    print(f"Ошибка: {e}")
except ValueError:
    print("Error: Некоррентный ввод")
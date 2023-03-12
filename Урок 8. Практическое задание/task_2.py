"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class ZeroDivisionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
try:
    dividend = float(input("Введите делимое: "))
    divisor = float(input("Введите делитель: "))
    if divisor == 0:
        raise ZeroDivisionError("Деление на ноль невозможно!")
    result = dividend / divisor
    print(f"Результат: {result}")
except ValueError:
    print("Ошибка: введите числа")
except ZeroDivisionError as e:
    print(f"Ошибка: {e.message}")

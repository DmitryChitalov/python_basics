"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class MyZeroDivision(Exception):
    def __init__(self, msg):
        self.msg = msg

try:
    divisible_num = int(input("Введите делимое число: "))
    devider = int(input("Введите делитель числа: "))

    if devider == 0:
        raise MyZeroDivision("Ошибка! Деление на ноль")
except ValueError:
    print("Ошибка! Нужно ввести целое число")
except MyZeroDivision as err:
    print(err)
else:
    print(f"Результат: ", divisible_num / devider)

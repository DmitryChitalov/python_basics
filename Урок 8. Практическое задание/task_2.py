"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self, my_message_error="Нельзя делить на ноль!"):
        self.my_message_error = my_message_error


try:
    first_value = int(input("Введите число для деления: "))
    second_value = int(input("Введите делитель: "))
    if second_value == 0:
        raise MyZeroDivisionError()
    result = first_value / second_value
    print("Результат деления:", result)
except MyZeroDivisionError as my_error:
    print(my_error.my_message_error)
except ValueError:
    print("Вам нужно вводить числа!")

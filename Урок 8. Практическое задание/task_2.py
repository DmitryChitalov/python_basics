"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


# define Python user-defined exceptions
class DevideByZero(Exception):
    def __str__(self):
        return f"На ноль делить нельзя"


# you need to guess this number
number = 18

try:
    input_num_a = int(input("Введите число a: "))
    input_num_b = int(input("Введите число b: "))
    if input_num_b == 0:
        raise DevideByZero
    else:
        print(f"Результат деления a на b {input_num_a / input_num_b}")
except ValueError:
    print("Вы ввели не число")
except DevideByZero as err:
    print(err)

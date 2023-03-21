Задание 2.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyError(Exception):
    def __init__(self, err):
        self.err = err

div_le = (input("Введите делимое: "))
div_r = (input("Введите делитель: "))

try:
    num_1 = int(div_le)
    num_2 = int(div_r)
    if num_2 == 0:
        raise MyError("Нельзя делить на ноль!")
except ValueError:
    print("Операция деления справедлива только для чисел! Введите число!")
except MyError as err:
    print(err)
else:
    result = num_1 / num_2
    print(f"{num_1} / {num_2} = {result}")
    
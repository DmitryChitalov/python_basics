"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


divisible = int(input("Введите делимое: "))
divider = int(input("Введите делитель: "))

try:
    divider = int(divider)
    if divider == 0:
        raise OwnError("На 0 делить нельзя!")
except OwnError as err:
    print(err)
else:
    print(f"Результат = {divisible / divider}")
finally:
    print("Работа программы завершена")

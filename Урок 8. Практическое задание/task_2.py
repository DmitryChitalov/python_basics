"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivZero(Exception):

    def __init__(self, txt):
        self.txt = txt


inp_data1 = float(input("Введите делимое: "))
inp_data2 = input("Введите делитель: ")

try:
    inp_data2 = float(inp_data2)
    if inp_data2 == 0:
        raise DivZero("Ошибка! Попытка деления на нуль!")
except DivZero as err:
    print(err)
else:
    print(f"Результат деления: {inp_data1 / inp_data2}")

"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class My_zerodiv_exception(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = input("Введите делимое: ")
divider = input("Введите делитель: ")
try:
    dividend = float(dividend)
    divider = float(divider)
    if divider == 0:
        raise My_zerodiv_exception("Вы ввели делитель равный нулю. На нуль делить нельзя!!")
except ValueError:
    print("Вы ввели не число")
except My_zerodiv_exception as err:
    print(err)
else:
    print(f"Ввод коректен. Частное: {dividend / divider}")

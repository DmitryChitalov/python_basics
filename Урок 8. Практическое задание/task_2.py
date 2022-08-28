"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class MyErrorZero(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = int(input("Введите число: "))
divider = int(input("Введите делитель: "))

try:
    if divider == 0:
        raise MyErrorZero("Деление на ноль!")

    result = inp_data / divider
except MyErrorZero as err:
    print(err)
else:
    print(f"Результат деления: {result}")
"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class MyDivByZero(Exception):
    def __init__(self, msg):
        self.msg = msg

try:
    input_devidend = int(input("Введите делимое число: "))
    input_devider = int(input("Введите делитель числа: "))

    if input_devider == 0:
        raise MyDivByZero("Оу-оу-оу, полегче паря!")
except ValueError:
    print("Вы ввели не число!")
except MyDivByZero as err:
    print(err)
else:
    print("А ты знаешь толк в цифрах ;)")
    print(f"Результат: ", input_devidend / input_devider)

"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
divided = input('Введите делимое: ')
divider = input('Введите делитель: ')
try:
    divided = int(divided)
    divider = int(divider)
    if divider == 0:
        raise OwnError("Деление на ноль недопустимо")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(divided / divider)
    

"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class DelError(Exception):
    def __init__(self, txt):
        self.txt = txt

dividend = int(input("Введите число - делимое: "))
divisor = int(input("Введите число - делитель: "))

try:
    if divisor == 0:
        raise DelError("На ноль делить нельзя!")
    res = int(dividend) / int(divisor)
except DelError as err:
    print(err)
else:
    print(f"Результат деления: {res}")
    

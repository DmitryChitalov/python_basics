"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    dividend = int(input("Введите число: "))
    divisor = int(input("Введите число: "))
    if divisor == 0:
        raise DivisionByZero("Нельзя делить на 0!")
    else:
        div = dividend / divisor
        print(div)
except DivisionByZero as e:
    print(e)


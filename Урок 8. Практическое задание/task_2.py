"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


nominator = int(input('Числитель: '))
denominator = int(input('Знаменатель: '))
try:
    if denominator == 0:
        raise MyError('Нельзя делить на 0!')
except MyError as err:
    print(err)
else:
    print(f'Результат: {nominator/denominator}')

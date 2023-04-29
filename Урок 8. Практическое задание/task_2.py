"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ErrorZeroNum(Exception):
    def __init__(self, user_num):
        self.user_num = user_num


numerator = int(input('Введите числитель: '))
denominator = int(input('Введите знаменатель: '))
try:
    if denominator == 0:
        raise ErrorZeroNum('Ошибочное деление.')

except ErrorZeroNum as ezn:
    print(ezn)
else:
    print(f'Результат деления: {numerator/denominator}')

"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class NumberEqualityZeroException(Exception):

    def __str__(self):
        return f'Число не должно равняться 0'


print('Вам необходимо ввести два числа a и b. Программа рассчитает результат операции деления a/b')

try:
    a = float(input('Введите a: '))
    b = float(input('Введите b: '))
    if b == 0:
        raise NumberEqualityZeroException
    print(f'результат деления a/b: {a / b}')
except NumberEqualityZeroException as e:
    print(f'{e}')
except ValueError:
    print('Ошибка формата данных')

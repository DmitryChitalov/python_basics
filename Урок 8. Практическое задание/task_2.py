"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class MyException(Exception):
    '''Исключения для деления на 0'''
    def __init__(self, msg):
        self.msg = msg

try:
    val_a = int(input('Введите Делимое: '))
    val_b = int(input('Введите Делитель: '))
    if val_b == 0:
        raise MyException('Делить на 0 нельзя!')
except ValueError:
    print('Вы ввели не число')
except MyException as err:
    print(err)
else:
    print(
        f'Результат вычисления выражения: {val_a / val_b}'
    )

"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException(Exception):
    txt = "Error"

    def __str__(self):
        return self.txt


number = int(input('Please enter number '))
devider = int(input('Please enter devider '))

try:
    if devider == 0:
        raise MyException
except MyException as err:
    print(err)
else:
    print(f'result of devision is {number / devider:.2f}')

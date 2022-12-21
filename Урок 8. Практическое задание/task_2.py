"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException(Exception):

    def __str__(self):
        return f"Недопустимое значение 0"


control = True
while control:
    try:
        num = int(input('Введите делитель '))
        if num == 0:
            raise MyException
        print(100 / num)
        print('Выходим из программы')
        control = False
    except MyException as e:
        print(e)

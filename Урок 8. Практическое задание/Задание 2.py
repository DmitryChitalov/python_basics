"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class Check(ZeroDivisionError):
    def __init__(self, text):
        self.text = text


try:
    imp = int(input('Enter one integer: '))
    if imp == 0:
        raise ValueError
    imp_1 = int(input('Enter 0: '))
    if imp_1 == 0:
        raise Check("Wrong, can't divide on zero")
except Check as err:
    print(err)
except ValueError:
    print('Wrong integer')

"""
Enter one integer: 100
Enter 0: 0
Wrong, can't divide on zero

Enter one integer: 0
Wrong integer
"""

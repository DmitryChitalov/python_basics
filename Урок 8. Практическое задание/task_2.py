"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyError(Exception):
    def __int__(self):
        self.a = a
        self.b = b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    if b == 0:
        raise MyError("You can't divide by 0")
    else:
        print(round(a / b))
except MyError as mr:
    print(mr)
except ValueError:
    print("Error type of value!")

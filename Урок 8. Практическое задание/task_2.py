"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyExceprionError(Exception):
    def __init__(self, text=None):
        if text == None:
            self.txt = "Деление на 0"
        else:
            self.txt = text

    def __str__(self):
        return f"MyExceprionError: {self.txt}"


try:
    a = int(input("Введитие делимое: "))
    b = int(input("Введитие делитель: "))
    if b == 0:
        raise MyExceprionError()
except MyExceprionError as error:
    print(error)

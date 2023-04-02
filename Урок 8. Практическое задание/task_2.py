"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class ZeroError(Exception):
    def __str__(self):
        return f'Ошибка 0'
class Del:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dell(self):
        if self.y == 0:
            raise ZeroError
        else:
            return self.x/self.y
d = Del(5, 0)
try:
    print(d.dell())
except ZeroError as exeption:
    print("Ошибка 0")

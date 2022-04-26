"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyDevZero(Exception):
    """ Деление на ноль
    Атрибуты 2 числа. Делимое и делитель
    """

    def __init__(self, my_var1, my_var2, message='Деление на ноль!'):
        self.my_var1 = my_var1
        self.my_var2 = my_var2
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Делитель {self.my_var2} -> {self.message}'


var1 = int(input('First number'))
var2 = int(input('Second number'))
if var2 == 0:
    raise MyDevZero(var1, var2)
print()

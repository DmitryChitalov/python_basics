"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroEroor(Exception):
    def __init__(self, txt):
        self.txt = txt


number_1 = int(input('Введите делимое  '))
number_2 = int(input('Введите делитель  '))

try:
    if number_2 == 0:
        raise ZeroEroor('Ошибка!!! Делитель равен 0')
except ZeroEroor as error:
    print(error)
else:
    result_1 = number_1 / number_2
    print(f'Результат деления: {result_1}')

"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class WorkWithZero(Exception):
    def __unit__(self, zero):
        self.zero = zero
number_one = int(input('Введите число: '))
number_two = int(input('Ведите второе число: '))
try:
    if number_two == 0:
        raise WorkWithZero()
    else:
        print((f"Результат: {number_one / number_two}"))
except WorkWithZero:
    print('Нельзя делить на ноль!')




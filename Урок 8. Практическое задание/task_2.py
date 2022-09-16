"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

# Выводим на экран задание
print('\nУрок 8 Задание 2\n')

# Объявляем класс
class DenominatorNotZero(Exception):
    def __init__(self, txt):
        self.txt = txt

# Определяем переменные
in_numerator = int(input('Введите числитель: '))
in_denominator = int(input('Введите знаминатель: '))

# Проверяем знаминатель и выводим результат
try:
    if in_denominator == 0:
        raise DenominatorNotZero('Знаминатель не может быть равен 0!')
except ValueError:
    print('Вы ввели не число')
except DenominatorNotZero as err:
    print (err)
else:
    print(f'{in_numerator} / {in_denominator} = {"{:.2f}".format(in_numerator / in_denominator)}')

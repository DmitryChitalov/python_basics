"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class ZeroDivException(Exception):
    def __init__(self, txt):
        self.txt = txt

def divide(numerator, denominator):
    if (denominator == 0):
        raise ZeroDivException("Деление на ноль")
    
    return numerator / denominator

try:
    numerator = float(input('Введите числитель: '))
    denominator = float(input('Введите знаменатель: '))
    print('Результат деления:', divide(numerator, denominator))

except ZeroDivException as e:
    print(e.txt)

print('Программа завершилась успешно')
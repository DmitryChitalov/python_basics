"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyExcept(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def div_err():
        try:
            a = float(input('Введите делимое: '))
            b = float(input('Введите делитель: '))
            if b == 0:
                raise MyExcept('Делить на ноль нельзя!')

            res = a / b
            return res
        except ValueError:
            return 'Ошибка ввода!'
        except Exception as err:
            return err


d = MyExcept
print('Результат: ', d.div_err())

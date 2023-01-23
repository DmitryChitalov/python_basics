"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class NoNullError(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def by_null(divider, denominator):
        try:
            if denominator == 0:
                raise NoNullError(f"Деление на ноль недопустимо")
            return divider / denominator
        except NoNullError as err:
            print(err)


rez1 = NoNullError.by_null(10, 0)
print(rez1)

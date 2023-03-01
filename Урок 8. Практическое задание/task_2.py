"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

def div_by_null():
    try:
        div = int(input('Ввести делимое: '))
        denominator = int(input('Ввод делителя: '))
        if denominator == 0:
            raise OwnError("Никак нельзя делить на ноль!")
        else:
            quotient = div / denominator
            return quotient
    except ValueError:
        return "Вы ввели совсем не число :("
    except OwnError as err:
        return err

print(div_by_null())

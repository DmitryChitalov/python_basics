"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class Own_error(Exception):
    def __init__(self, txt):
        self.txt = txt

def div_by_null():
    try:
        div = int(input('Ввод делимого: '))
        denominator = int(input('Ввод делителя: '))
        if denominator == 0:
            raise Own_error("На ноль делить нельзя")
        else:
            quotient = div / denominator
            return quotient
    except ValueError:
        return "Введено не число"
    except Own_error as err:
        return err

print(div_by_null())

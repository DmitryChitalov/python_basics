"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class Dichotomy(Exception):
    def __init__(self, data):
        self.data = data


def div_num():
    try:
        num_a = int(input("Введите первое число: "))
        num_b = int(input("Введите второе число: "))
        if num_b == 0:
            raise Dichotomy("Нельзя делить на ноль")
        else:
            num_c = num_a / num_b
            return num_c
    except ValueError:
        return "Данные введены некорректно"
    except Dichotomy as fatal_error:
        return fatal_error


print(div_num())
"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        user_num_1 = int(input('Введите делимое: '))
        user_num_2 = int(input('Введите делитель: '))
        if user_num_2 == 0:
            raise OwnError("Делить на ноль нельзя!")
        else:
            res = user_num_1 / user_num_2
            return res
    except ValueError:
        return "Необходимо ввести число!"
    except OwnError as err:
        return err


print(div())

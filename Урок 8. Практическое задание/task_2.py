"""
Задание 2.
Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ErrorHandle:
    def __init__(self, var_1, var_2):
        self.var_1 = var_1
        self.var_2 = var_2

    def div(var_1, var_2):
        try:
            if var_1 == 0 or var_2 == 0:
                return "Вы пытаетесь делить на 0!"
        except ErrorHandle as err:
            print(err)
        else:
            div_res = var_1 / var_2
            return div_res


var_1 = int(input("Введите первое число: "))
var_2 = int(input("Введите второе число: "))
print(ErrorHandle.div(var_1, var_2))



"""
Задание 2.
Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class Zero_divis:
    def __init__(self, var_1, var_2):
        self.var_1 = var_1
        self.var_2 = var_2

    def divis(var_1, var_2):
        if var_1 > 0 and var_2 > 0:
            divis = var_1 / var_2
            return divis
        else:
            return "Вы пытаетесь делить на 0!"


print(Zero_divis.divis(0, 5))
print(Zero_divis.divis(15, 6))
print(Zero_divis.divis(75, 0))



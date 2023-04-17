"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class DivByNull:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider
  
    def div_by_null(self):
        try:
            return f'Результат деления = {self.dividend / self.divider}'
        except:
            return (f"Ошибка. Вы пытаетесь делить на ноль")

obj_by_null = DivByNull(150, 0)
print(obj_by_null.div_by_null())

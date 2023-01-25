"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class DivisionByNull:
    def __init__(self, divide, denominator):
        self.divide = divide
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divide, denominator):
        try:
            return (divide / denominator)
        except:
            return (f"На ноль делить !НЕЛЬЗЯ!")


div = DivisionByNull(20, 100)
print(f'1-й пример 400 / 20 = {DivisionByNull.divide_by_null(400, 20)}')
print(f'2-й пример 20 / 0: {DivisionByNull.divide_by_null(20, 0)}')

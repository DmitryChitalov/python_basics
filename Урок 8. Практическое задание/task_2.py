"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class MyZeroDivizionError(Exception):
    
    def __init__(self) -> None:
        self.message = "Are you seriously try divide on zero?"
        super().__init__(self.message)

class Sample:
    
    @staticmethod
    def divide_number(first, second) -> float:
        try:
            if second == 0:
                raise MyZeroDivizionError()
            else:
                return first / second
        except MyZeroDivizionError as error:
            print(error)
            return 0



print(Sample.divide_number(10, 2))
print(Sample.divide_number(15, 0))
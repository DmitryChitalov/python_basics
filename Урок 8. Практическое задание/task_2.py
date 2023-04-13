"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class Dividebyzero:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def division(self, num1, num2):
        try:
            return num1 / num2
        except:
            return (f"cannot divide by zero")


div = Dividebyzero(1, 0)
print(div.division(50, 0))
print(div.division(50, 25))
print(div.division(100, 0))

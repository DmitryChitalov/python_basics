# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class DivisionByZeroError(Exception):
    def __init__(self, message="Делить на ноль нельзя"):
        self.message = message
        super().__init__(self.message)


def divide(a, b):
    if b == 0:
        raise DivisionByZeroError()
    return a / b

try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    result = divide(a, b)
    print(f"Результат: {result}")
except DivisionByZeroError as e:
    print(e)
except ValueError:
    print("Ошибка ввода: введите число")


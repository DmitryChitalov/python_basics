"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class CustomZeroDivisionError(Exception):
    """info"""

def get_numerator() -> int:
    """info"""
    return int(input("Введите числитель >>> "))


def get_denominator() -> int:
    """info"""
    value = int(input("Введите знаменатель >>> "))

    if value == 0:
        raise CustomZeroDivisionError

    return value


while True:
    try:
        numerator = get_numerator()
        denominator = get_denominator()

        print(f"Результат = {numerator / denominator}")
    except CustomZeroDivisionError:
        print("на 0 делить нельзя")
    except KeyboardInterrupt:
        break

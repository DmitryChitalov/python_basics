"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class CustomZeroDivisionError(Exception):
    pass


def get_numerator() -> int:
    return int(input("Введите числитель >>> "))


def get_denominator() -> int:
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
        print("Вы ввели 0 в качестве знаменателя, так не пойдет")
    except KeyboardInterrupt:
        break
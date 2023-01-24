"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivTest(ZeroDivisionError):
    text = "Деление на ноль запрещено"

    def __str__(self):
        return self.text


try:
    dividend = float(input("Введите число-делимое: "))
    divisor = float(input("Введите число-делитель: "))
    if divisor == 0:
        raise ZeroDivTest
    print(f"{dividend} / {divisor} = {dividend / divisor}")
except ZeroDivTest:
    print(ZeroDivTest.text)
except ValueError:
    print("В качестве аргументов введите числа")
finally:
    print("Программа завершена")
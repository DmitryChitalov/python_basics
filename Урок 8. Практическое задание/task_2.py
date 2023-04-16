"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class nondivide(Exception):
    pass
while True:
    try:
        dividend = int(input("Введите число которое хотите поделить: "))
        divisor = int(input("Введите на сколько хотите поделить: "))
        if divisor == 0:
            raise nondivide("Не может делиться на 0")
        result = dividend / divisor
        print(f"{dividend}/{divisor} = {result}")
        break
    except ValueError:
        print("Please enter integers")
    except nondivide as error:
        print(error)

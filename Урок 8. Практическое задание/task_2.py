"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class CustomZeroDivisionError(Exception):
    pass

try:
    user_input = input("Пожалуйста, введите два числа через пробел для операции деления: ").split(" ")
    if int(user_input[1]) == 0:
        raise CustomZeroDivisionError()
    print(f"Результат деления: {int(user_input[0]) / int(user_input[1])}")
except CustomZeroDivisionError as custom_error:
    print(f"Вы ввели {user_input[1]} в качестве делителя. Делить на ноль нельзя.")

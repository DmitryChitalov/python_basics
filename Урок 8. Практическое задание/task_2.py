"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class MyDivZero(Exception):
    def __init__(self):
        print("Мой обработчик деления на ноль")
        return

    @staticmethod
    def test_div_zero(divider):
        """
        Тестирует делитель (число) на равенство нулю.
        :param divider: делитель
        :return: True - если делитель равен нулю, False - если делитель не равен нулю
        """
        return not divider


try:
    a = int(input("Введите делимое:"))
    b = int(input("Введите делитель:"))
    if MyDivZero.test_div_zero(b):
        raise MyDivZero
except MyDivZero:
    print("На ноль делить нельзя!")
except ValueError:
    print("Некорректный ввод!")
else:
    z = a / b
    print(f"Результат деления: {a} / {b} = {z}")
finally:
    print("Работа программы завершена.")

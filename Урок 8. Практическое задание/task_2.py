"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class My_ZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    n = int(input("На скольких человек будем делить 200 яблок? "))
    if n == 0:
        raise My_ZeroDivisionError("На ноль делить нельзя")
except My_ZeroDivisionError as e:
    print(e)
else:
    print(f"Каждому достанется по {200 / n} яблок(а)")

"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, another):
        return f'Сложение: {self.a + another.a} + ({self.b + another.b} * i)'

    def __mul__(self, another):
        return f'Умножение: {self.a * another.a - (self.b * another.b)} + ({self.b * another.a} * i) '


c_1 = Complex_number(155, -13)
c_2 = Complex_number(129, -119)
print(c_1 + c_2)
print(c_1 * c_2)

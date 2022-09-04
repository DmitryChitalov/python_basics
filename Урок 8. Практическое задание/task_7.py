"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма z1 и z2:')
        if self.b + other.b < 0:
            sign = ""
        else:
            sign = "+"
        return f'z1+z2 = {self.a + other.a}{sign}{self.b + other.b}i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2:')
        if self.a * other.b + self.b * other.a < 0:
            sign = ""
        else:
            sign = "+"
        return f'z1*z2 = {self.a * other.a - self.b * other.b}{sign}{self.a * other.b + self.b * other.a}i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z1 = ComplexNumber(-2, -3)
z2 = ComplexNumber(1, -2)
print(z1 + z2)
print(z1 * z2)

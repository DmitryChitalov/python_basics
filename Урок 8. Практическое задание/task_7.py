"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
import self as self


class Complex:
    def __init__(self, real, imag):
        self.re = real
        self.im = imag

    def __add__(self, o):
        return Complex(self.re + o.re, self.im + o.im)

    def __mul__(self, o):
        return Complex(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def __str__(self):
        if self.im == 0:
            return '%.2f' % self.re
        if self.re == 0:
            return '%.2fi' % self.im
        if self.im < 0:
            return '%.2f - %.2fi' % (self.re, -self.im)
        else:
            return '%.2f + %.2fi' % (self.re, self.im)


a = Complex(2, 3)
b = Complex(5, -2)
print(a + b)
print(a * b)

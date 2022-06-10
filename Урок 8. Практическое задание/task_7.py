"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:

    def __init__(self, real: float = 0, imaginary: float = 0):
        if not (isinstance(real, float) or isinstance(real, int)):
            raise ValueError('The real part must be a number')
        if not (isinstance(imaginary, float) or isinstance(imaginary, int)):
            raise ValueError('The imaginary component must be a number')
        self.re = real
        self.im = imaginary

    def __str__(self):
        return f'{self.re} + i{self.im}' if self.im >=0 else f'{self.re} - i{abs(self.im)}'

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im - self.im * other.re)


if __name__ == '__main__':
    c1 = Complex(1, 1)
    c2 = Complex(2, -4)
    print(f'c1 = {c1}, c2 = {c2}')
    print(f'c1 + c2 = {c1 + c2}')
    print(f'c1 * c2 = {c1 * c2}')




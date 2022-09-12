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
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNumber(a, b)

    def __mul__(self, other):
        a = (self.a * other.a) - (self.b * other.b)
        b = (self.a * other.b) + (self.b * other.a)
        return ComplexNumber(a, b)

    def __str__(self):
        return f'{self.a} + {self.b}j'


x1 = ComplexNumber(2, 5)
x2 = ComplexNumber(3, 9)
print(f'Первое число: {x1}')
print(f'Второе число: {x2}')
print(f'Сложение чисел: {x1 + x2}')
print(f'Умножение чисел: {x1 * x2}')

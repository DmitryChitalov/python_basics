"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

# pylint: disable=missing-class-docstring, missing-function-docstring,multiple-statements,invalid-name


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
        return f"{self.a} + {self.b}j"


one = ComplexNumber(3, 9)
two = ComplexNumber(5, 2)
print(f"Первое число: {one}")
print(f"Второе число: {two}")
print(f"Сложение чисел: {one + two}")
print(f"Умножение чисел: {one * two}")

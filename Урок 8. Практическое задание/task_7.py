"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        print('\nСумма равна')
        return ComplexNumber(
            self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        print('\nПроизведение равно')
        return ComplexNumber(
            (self.real * other.real) - (self.imaginary * other.imaginary),
            (self.imaginary * other.real) + (self.real * other.imaginary))

    def __str__(self):
        return f'{self.real} + {self.imaginary}i'


num1 = ComplexNumber(1, 2)
num2 = ComplexNumber(3, 4)
print(f"a = {num1}")
print(f"b = {num2}")
print(num1 + num2)
print(num1 * num2)

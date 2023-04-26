"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class MyClass:

    def __init__(self, real, imaginary_number):
        self.r = real
        self.i = imaginary_number

    def __add__(self, other):
        return MyClass(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return MyClass((self.r * other.r - self.i * other.i), (self.r * other.i + other.r * self.i))

    def __str__(self):
        return f'{self.r}{"+" if self.i > 0 else ""}{self.i}i'


complex_number_1 = MyClass(1, 2)
complex_number_2 = MyClass(3, -1)
print(complex_number_1 + complex_number_2)
print(complex_number_1 * complex_number_2)

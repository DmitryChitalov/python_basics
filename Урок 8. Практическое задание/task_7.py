"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part,
                             self.imaginary_part + other.imaginary_part)

    def __mul__(self, other):
        real = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        imaginary = self.real_part * other.imaginary_part + self.imaginary_part * other.real_part
        return ComplexNumber(real, imaginary)

    def __str__(self):
        return f"{self.real_part} + {self.imaginary_part}i"

c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(-1, 5)

print(c1 + c2) # 1 + 8i
print(c1 * c2) # -17 + 1i

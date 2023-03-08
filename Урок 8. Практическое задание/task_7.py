"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = int(imag)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)

    def __str__(self):
        return f"({self.real}+{self.imag}j)"


# Пример использования и проверка результата
c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, 4)

print(c1 + c2, complex(1, 2) + complex(3, 4))  # (4+6j) (4+6j)
print(c1 * c2, complex(1, 2) * complex(3, 4))  # (-5+10j) (-5+10j)

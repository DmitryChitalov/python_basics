"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    real: float
    indeterminate: float

    def __init__(self, real: float, indeterminate: float):
        self.real = real
        self.indeterminate = indeterminate

    def __add__(self, other: 'ComplexNumber'):
        return ComplexNumber(
            self.real + other.real,
            self.indeterminate + other.indeterminate
        )

    def __mul__(self, other: 'ComplexNumber'):
        r1 = self.real * other.real
        r2 = self.indeterminate * other.indeterminate * -1

        i1 = self.real * other.indeterminate
        i2 = self.indeterminate * other.real

        real = r1 + r2
        indeterminate = i1 + i2

        return ComplexNumber(real, indeterminate)

    def __str__(self):
        return f"({self.real}{'+' if self.indeterminate > 0 else ''}{self.indeterminate}i)"


a = ComplexNumber(4, 55)
b = ComplexNumber(6, 22)

# (4+55i) + (6+22i) = (4 + 6) + (55 + 22)i = (10+77i)
print(a + b)

# (4+55i) * (6+22i) = (4 * 6) + (4 * 22i) + (55 * 6i) + (55 * 22i^2) = 24 + 88i + 330i - 1210 = (-1186+418i)
print(a * b)
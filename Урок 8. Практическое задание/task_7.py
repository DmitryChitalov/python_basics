"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class ComplexNumbers:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im < 0:
            return f"({self.re}{self.im}i)"
        else:
            return f"({self.re}+{self.im}i)"

    def __add__(self, other):
        return ComplexNumbers(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumbers(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)


# проверка в сравнении со встроенным типом complex
a = complex(3, 2)
a_1 = ComplexNumbers(3, 2)
b = complex(5, -6)
b_1 = ComplexNumbers(5, -6)

c = a + b
c_1 = a_1 + b_1

d = a * b
d_1 = a_1 * b_1

print(f"{a} + {b} = {c}")
print(f"{a_1} + {b_1} = {c_1}")
print(f"{a} * {b} = {d}")
print(f"{a_1} * {b_1} = {d_1}")

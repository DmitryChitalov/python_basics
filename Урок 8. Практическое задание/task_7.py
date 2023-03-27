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
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber((self.a * other.a - self.b * other.b),
                             (self.a * other.b + self.b * other.a))

    def __str__(self):
        return f'{self.a}{"+" if self.b > 0 else "-"}{abs(self.b)}*i'


cn_1 = ComplexNumber(2, -5)
cn_2 = ComplexNumber(-3, -2)

print(f'({cn_1}) + ({cn_2}) = {cn_1 + cn_2}')
print(f'({cn_1}) * ({cn_2}) = {cn_1 * cn_2}')

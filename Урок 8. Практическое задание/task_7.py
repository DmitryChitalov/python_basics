"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNum:

    def __init__(self, num_a, num_b):
        self.num_a = num_a
        self.num_b = num_b

    def __add__(self, other):
        a = self.num_a + other.num_a
        b = self.num_b + other.num_b
        return ComplexNum(a, b)

    def __mul__(self, other):
        a = self.num_a * other.num_a - self.num_b * other.num_b
        b = self.num_b * other.num_a + self.num_a * other.num_b
        return ComplexNum(a, b)

    def __str__(self):
        return f'{self.num_a}+{self.num_b}j'


complex_1 = ComplexNum(7, 3)
complex_2 = ComplexNum(6, 2)

print(f'{complex_1} + {complex_2} = {complex_1 + complex_2}')
print(f'{complex_1} * {complex_2} = {complex_1 * complex_2}')

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
        return f'{self.a} + {self.b}i'


if __name__ == '__main__':
    z1 = ComplexNumber(4, 5)
    z2 = ComplexNumber(6, 7)
    z3 = z1 + z2
    z4 = z1 * z2
    print(f'Первое  число: z1 = {z1}')
    print(f'Второе  число: z2 = {z2}')
    print(f'Сложение  чисел: z1 + z2 = {z3}')
    print(f'Умножение  чисел: z1 * z2 = {z4}')


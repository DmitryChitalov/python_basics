"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNum(a, b)
    def __mul__(self, other):
        a = (self.a * other.a) - (self.b * other.b)
        b = (self.a * other.b) + (self.b * other.a)
        return ComplexNum(a, b)
    def __str__(self):
        return f'{self.a} + {self.b}j'
if __name__ == '__main__':
    c1 = ComplexNum(4, 8)
    c2 = ComplexNum(6, 9)
    c3 = c1 + c2
    c4 = c1 * c2
    print(f'Комплексное число один: {c1}')
    print(f'Комплексное число два: {c2}')
    print(f'Сложение : {c3}')
    print(f'Умножение : {c4}')


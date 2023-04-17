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
        return f'z1 + z2 = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'z1 * z2 = {self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a} * i'

    def __str__(self):
        return f'= {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, 5)
z_2 = ComplexNumber(2, 4)
print(f'z1 {z_1}')
print(f'z2 {z_2}')
print(z_1 + z_2)
print(z_1 * z_2)
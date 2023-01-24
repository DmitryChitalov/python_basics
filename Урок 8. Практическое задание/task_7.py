"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNumber:

    def __init__(self, a, b):
            self.a = float(a)
            self.b = float(b)
            self.z = f'{self.a} + {self.b} * i'

    def __add__(self, other):
        print(f'Сложение комплексных чисел\nЧисло 1: {self.z}\nЧисло 2: {other.z}')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел\nЧисло 1: {self.z}\nЧисло 2: {other.z}')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


complex_1 = ComplexNumber(1, 2)
complex_2 = ComplexNumber(3, 4)
print(complex_1 + complex_2)
print(complex_1 * complex_2)
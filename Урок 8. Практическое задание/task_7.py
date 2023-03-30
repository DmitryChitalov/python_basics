"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNumber:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        return f'({self.a:.2f} + {self.b:.2f}i)'
    
    def __add__(self, other):
        result = ComplexNumber(self.a + other.a, self.b + other.b)
        print(f'{self} + {other} = {result}')
        return result
    
    def __sub__(self, other):
        result = ComplexNumber(self.a - other.a, self.b - other.b)
        print(f'{self} - {other} = {result}')
        return result

    def __mul__(self, other):
        result = ComplexNumber(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)
        print(f'{self} * {other} = {result}')
        return result

    def __truediv__(self, other):
        denominator = other.a ** 2 + other.b ** 2
        result = ComplexNumber((self.a * other.a + self.b * other.b) / denominator, (self.b * other.a - self.a * other.b) / denominator)
        print(f'{self} / {other} = {result}')
        return result

n1 = ComplexNumber(-1.2, 0.4) + ComplexNumber(2, 0)
n2 = n1 - ComplexNumber(1, 29)
n3 = ComplexNumber(12, 3.0) * n2
n4 = n3 / n2



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
    
    def __str__(self):
        return f'Комплексное число: {complex(self.a, self.b)}'

    def __add__(self, other):
        return f'Сумма комплексных чисел: {complex((self.a + other.a),(self.b + other.b))}'
    
    def __mul__(self, other):
        return f'Произведение комплексных чисел: {complex((self.a * other.a - self.b * other.b), (self.a * other.b + self.b * other.a))}'

complex_number_1 = ComplexNumber(2, 5)
complex_number_2 = ComplexNumber(1, -3)

print(complex_number_1)
print(complex_number_2)

print(complex_number_1 + complex_number_2)
print(complex_number_1 * complex_number_2)

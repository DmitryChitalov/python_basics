"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class ComplexNums:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNums(a, b)
    def __mul__(self, other):
        a = (self.a * other.a) - (self.b * other.b)
        b = (self.a * other.b) + (self.b * other.a)
        return ComplexNums(a, b)
    def __str__(self):
        return f'{self.a} + {self.b} * i'

num_1 = ComplexNums(10, 7)
num_2 = ComplexNums(4, 8)
print(f'Результат сложения чисел: = {num_1 + num_2}')
print(f'Результат произведения чисел: = {num_1 * num_2}')
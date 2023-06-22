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
        return f'Сумма: {self.a + other.a} + {self.b + other.b}i'


    def __mul__(self, other):
        return f'Произведение: {(self.a * other.a) - (self.b * other.b)} {self.b * other.a}i'
               

    def __str__(self):
        return f'{self.a}{"+" if self.b > 0 else ""}{self.b}i'

first_numbers = ComplexNumber(8, 6)
second_numbers = ComplexNumber(-98, 7)
print(first_numbers + second_numbers)
print(first_numbers * second_numbers)

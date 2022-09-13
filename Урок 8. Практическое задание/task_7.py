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
        self.z = 'a + b * i'

    def __add__(self, other):
        return f'Результат сложения комлексных чисел: {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'Результат умножения комлексных чисел: {self.a * other.a - (self.b * other.b) + (self.b * other.a)}i' \
               f'+{self.b * other.a}i'


first_numbers = ComplexNumber(233, 4)
second_numbers = ComplexNumber(12, 132)
print(first_numbers * second_numbers)
print(first_numbers + second_numbers)

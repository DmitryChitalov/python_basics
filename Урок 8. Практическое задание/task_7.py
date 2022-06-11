"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма a и b равна')
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        print(f'Произведение a и b равно')
        return f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a}i'

    def __str__(self):
        return f'{self.a} + {self.b}i'


a = ComplexNumber(1, -2)
b = ComplexNumber(3, 4)
print(f"a = {a}")
print(f"b = {b}")
print(a + b)
print(a * b)
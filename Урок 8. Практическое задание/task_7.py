"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class ComplexNumber:
    def __init__(self, x, y, *args):
        self.x1 = x
        self.x2 = y

    def __add__(self, other):
        print(f'Сложение комплексных чисел')
        return f'x = {self.x1 + other.x1} + {self.x2 + other.x2} '

    def __mul__(self, other):
        print(f'Умножение комплексных чисел')
        return f'x = {self.x1 * other.x1 - (self.x2 * other.x2)} + {self.x2 * other.x1} '

    def __str__(self):
        return f'x = {self.x1} + {self.x2} '

x1 = ComplexNumber(1, 2)
x2 = ComplexNumber(3, 4)
print(x1 + x2)
print(x1 * x2)

"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} + ( {self.y} * i )"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Complex(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Complex(x, y)


x1 = Complex(5, -3)
x2 = Complex(5, 5)

print(x1)
print(x2)
print(x1 + x2)
print(x1 * x2)
print(x1)
print(x2)

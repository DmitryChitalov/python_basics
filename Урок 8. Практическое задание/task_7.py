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
        return f"{self.a} + {self.b}i"

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)


a1 = int(input("a1: "))
b1 = int(input("b1: "))
a2 = int(input("a2: "))
b2 = int(input("b2: "))
cobj_1 = ComplexNumber(a1, b1)
cobj_2 = ComplexNumber(a2, b2)

print(f"Первое комплексное число: {cobj_1}")
print(f"Второе комплексное число: {cobj_2}")
print(f"Сумма двух чисел: {cobj_1 + cobj_2}")
print(f"Произведение двух чисел: {cobj_1 * cobj_2}")

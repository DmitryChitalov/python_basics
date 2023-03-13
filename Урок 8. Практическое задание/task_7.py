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
        return f'Это комплексное число: {self.a}+({self.b}*i)'

    def __add__(self, other):
        res_a = self.a + other.a
        res_b = self.b + other.b
        return ComplexNumber(res_a, res_b)

    def __mul__(self, other):
        res_a = self.a * other.a - self.b * other.b
        res_b = self.b * other.a + self.a * other.b
        return ComplexNumber(res_a, res_b)

c_numb_1 = ComplexNumber(4, -8)
c_numb_2 = ComplexNumber(6, 11)
y = c_numb_1 + c_numb_2
x = c_numb_1 * c_numb_2
z = x + y
print(y, x, z, sep='\n')

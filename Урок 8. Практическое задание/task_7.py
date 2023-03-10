"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class ComplexNum:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f'z = {self.x + other.x} + {self.y + other.y}i'

    def __mul__(self, other):
        return f'z = {self.x * other.x - (self.y * other.y)} + {self.x * other.y}i'


z_1 = ComplexNum(1, -2)
z_2 = ComplexNum(3, 4)
print(z_1 + z_2)
print(z_1 * z_2)
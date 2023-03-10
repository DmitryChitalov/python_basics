"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class Complex_number:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, another):
        return f'Сумма: {self.x + another.x} + ({self.y + another.y} * i)'

    def __mul__(self, another):
        return f'Произведение: {self.x * another.x - (self.y * another.y)} + ({self.y * another.x} * i)'


z_1 = Complex_number(12, -3)
z_2 = Complex_number(27, 7)
print(z_1 + z_2)
print(z_1 * z_2)
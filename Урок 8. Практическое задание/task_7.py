"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class ComplexNumber:
    def __init__(self, k, y, *args):
        self.k = k
        self.y = y
        self.q = 'k + y * i'

    def __add__(self, other):
        print(f'Сумма q1 и q2:')
        return f'q = {self.k + other.k} + {self.y + other.y} * i'

    def __mul__(self, other):
        print(f'Произведение q1 и q2:')
        return f'q = {self.k * other.k - (self.y * other.y)} + {self.y * other.y} * i'

    def __str__(self):
        return f'q = {self.k} + {self.y} * i'


q1 = ComplexNumber(2, -8)
q2 = ComplexNumber(7, 3)
print(q1 + q2)
print(q1 * q2)

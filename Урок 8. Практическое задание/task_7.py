"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class ComplexNumber:

    def __init__(self, num, inum):
        self.num = num
        self.inum = inum

    def __add__(self, other):
        return ComplexNumber(self.num + other.num, self.inum + other.inum)

    def __mul__(self, other):
        # (2 - 7i) * (3 + 5i)
        return ComplexNumber((self.num * other.num - self.inum * other.inum), (self.num * other.inum + other.num * self.inum))

    def __str__(self):
        return f'{self.num}{"+" if self.inum > 0 else ""}{self.inum}i'


complex_1 = ComplexNumber(2, -7)
complex_2 = ComplexNumber(3, 5)

print(complex_1 + complex_2)
print(complex_1 * complex_2)
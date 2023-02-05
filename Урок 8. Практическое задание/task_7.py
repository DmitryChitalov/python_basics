'''
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''
class INumbers:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return INumbers(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return INumbers(self.real * other.real - self.imaginary * other.imaginary,
                        self.real * other.imaginary + self.imaginary * other.real)

    def __str__(self):
        if self.imaginary == 0:
            return f'{self.real}'
        sign = '+' if self.imaginary > 0 else '-'
        return f'({self.real} {sign} {abs(self.imaginary)}i)'


num1 = INumbers(-11, 15)
num2 = INumbers(7, -91)
print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} * {num2} = {num1 * num2}')
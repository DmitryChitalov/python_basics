"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return ComplexNumber(x, y)
    def __mul__(self, other):
        x = (self.x * other.x) + (self.y * other.y)
        y = (self.x * other.y) + (self.y * other.x)
        return ComplexNumber(x, y)
    def __str__(self):
        return f'{self.x} + {self.y}'
if __name__ == '__main__':
    Num1 = ComplexNumber(25, 12)
    Num2 = ComplexNumber(6, 10)
    Num3 = Num1 + Num2
    Num4 = Num1 * Num2


    print(f'Первое число Num1 = {Num1}')
    print(f'Второе число Num2 = {Num2}')
    print(f'Операция сложение чисел: Num1 + Num2 = {Num3}')
    print(f'Операция умножение чисел: Num1 * Num2 = {Num4}')
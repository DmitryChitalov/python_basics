"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class ComplexNumber:
    # создание атрибутов x и y для класса ComplexNumber
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return ComplexNumber(x, y)

    def __mul__(self, other):
        x = (self.x * other.x) - (self.y * other.y)
        y = (self.x * other.y) + (self.y * other.x)
        return ComplexNumber(x, y)

    def __str__(self):
        return f'{self.x} + {self.y}i'

n = ComplexNumber(5, 7)
m = ComplexNumber(2, 9)
print(f'Первое число равно: n = {n}')
print(f'Второе число равно: m = {m}')
print(f'Результат сложения чисел: n + m = {n + m}')
print(f'Результат произведения чисел: n * m = {n * m}')
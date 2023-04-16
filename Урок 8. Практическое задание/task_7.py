"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)
    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}"
        else:
            return f"{self.real} - {-self.imaginary}"

num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(2, -2)

print(f"Первое число: {num1}")
print(f"Второе число: {num2}")

summa = num1 + num2
print(f"Сумма: {summa}")

product = num1 * num2
print(f"Произведение: {product}")


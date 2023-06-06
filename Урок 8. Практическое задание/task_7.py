class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        # Сложение комплексных чисел
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __mul__(self, other):
        # Умножение комплексных чисел
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def __str__(self):
        # Возвращаем строковое представление комплексного числа
        return f"{self.real} + {self.imaginary}i"

# Создаем два комплексных числа
complex1 = ComplexNumber(2, 3)
complex2 = ComplexNumber(1, -2)

# Сложение комплексных чисел
sum_result = complex1 + complex2
print(f"Результат сложения: {sum_result}")

# Умножение комплексных чисел
multiply_result = complex1 * complex2
print(f"Результат умножения: {multiply_result}")

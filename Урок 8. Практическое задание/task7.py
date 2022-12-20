class ComplexNumber:
    def __init__(self, real_numb, imaginary_numb):
        self.real_numb = real_numb
        self.imaginary_numb = imaginary_numb

    def __add__(self, other):
        return self.real_numb + other.real_numb, self.imaginary_numb + other.imaginary_numb

    def __mul__(self, other):
        return self.real_numb * other.real_numb - self.imaginary_numb * other.imaginary_numb, self.real_numb * other.imaginary_numb + other.real_numb * self.imaginary_numb

a = ComplexNumber(3, -5)
b = ComplexNumber(4, 2)
c = a + b
d = a * b
print(f"Разница комплексных чисел: {c[0]} + ({c[1]})i")
print(f"Умножение комплексных чисел: {d[0]} + ({d[1]})i")
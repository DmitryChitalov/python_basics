class ComplexNumber:
    def __init__(self, real_part, imag_part):
        self.real = real_part
        self.imag = imag_part

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.imag * other.real + self.real * other.imag)

    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real}{sign}{abs(self.imag)}i"


c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, -4)

c_sum = c1 + c2
print(f"Сумма комплексных чисел {c1} и {c2} равна {c_sum}")

c_prod = c1 * c2
print(f"Произведение комплексных чисел {c1} и {c2} равно {c_prod}")

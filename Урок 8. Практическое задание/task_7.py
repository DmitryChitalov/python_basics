class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real - self.imaginary * other.imaginary),
                             (self.real * other.imaginary + other.real * self.imaginary))

    def __str__(self):
        return f'{self.real}{"+" if self.imaginary > 0 else ""}{self.imaginary}i'


cn_1 = ComplexNumber(1, -2)
cn_2 = ComplexNumber(3, 4)

print(cn_1 + cn_2)
print(cn_1 * cn_2)

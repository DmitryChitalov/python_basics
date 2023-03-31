# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real_part, imag_part):
        self.real_part = real_part
        self.imag_part = imag_part

    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part, self.imag_part + other.imag_part)

    def __mul__(self, other):
        return ComplexNumber(self.real_part * other.real_part - self.imag_part * other.imag_part,
                             self.real_part * other.imag_part + self.imag_part * other.real_part)

    def __str__(self):
        if self.imag_part < 0:
            return f"{self.real_part} - {-self.imag_part}i"
        else:
            return f"{self.real_part} + {self.imag_part}i"
# создание комплексных чисел
c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, -1)
print(c1)
print(c2)

# сложение комплексных чисел
c3 = c1 + c2
print(c3) # 4 + 1i

# умножение комплексных чисел
c4 = c1 * c2
print(c4) # 5 - 1i

"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:
    """Комплексное число"""
    def __init__(self, num_a, num_b=1) -> None:
        self.num_a = num_a
        self.num_b = num_b

    def __add__(self, other):
        return Complex(self.num_a + other.num_a, self.num_b + other.num_b)

    def __mul__(self, other):
        return Complex(self.num_a * other.num_a - self.num_b * other.num_b,
                       self.num_a * other.num_b + self.num_b * other.num_a)

    def __str__(self) -> str:
        a_res = '' if self.num_a == 0 else self.num_a
        b_sign = '' if self.num_a == 0 or self.num_b == 0 else \
            "+" if self.num_b > 0 else "-"
        b_res = '' if self.num_b == 0 else \
            f"{abs(self.num_b) if abs(self.num_b) != 1 else ''}i"
        result = f"{a_res}{b_sign}{b_res}"
        return '0' if result == '' else result


comp_1 = Complex(-9, -7)
comp_2 = Complex(-1)
print(f"z1 = {comp_1}")
print(f"z2 = {comp_2}")
print(f"z1 + z2 = {comp_1 + comp_2}")
print(f"z1z2 = {comp_1 * comp_2}")

comp_3 = Complex(2, 3)
print(f"z3 + z2 = {comp_3 + comp_2}")
print(f"z3z2 = {comp_3 * comp_2}")

comp_4 = Complex(2, 0)
comp_5 = Complex(-2, 0)
print(f"z4 + z5 = {comp_4 + comp_5}")
print(f"z4z5 = {comp_4 * comp_5}")

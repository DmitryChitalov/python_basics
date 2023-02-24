class Complexnumber:
    def __init__(self, a, b,):
        self.a = a
        self.b = b

#(a + bi) ± (c + di) = (a ± c) + (b ± d)i
    def __add__(self, other):
        return f'Сумма комплексных чисел:\n ' \
               f'{self.a + other.a} + {self.b + other.b}*i'

# (a + bi) · (c + di) = (ac – bd) + (ad + bc)i
    def __mul__(self, other):
        return f'Произведение комплексных чисел:\n' \
               f' {self.a * other.a - self.b * other.b} + ' \
               f'{self.a * other.b + self.b * other.a}*i'

z_1 = Complexnumber(5, 3)
z_2 = Complexnumber(4, -7)
print(z_1 + z_2)
print(z_1 * z_2)
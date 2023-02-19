"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
#z = a + bi
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

"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        # Для более лаконичного вывода избавимся от лишнего знака при отрицательном значении
        if self.b + other.b < 0:
            return f'Сумма равна: {self.a + other.a} - {abs(self.b + other.b)} * i'
        return f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        if self.b * other.a < 0:
            return f'Произведение равно: {self.a * other.a - (self.b * other.b)} - {abs(self.b * other.a)} * i'
        return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


number_1 = ComplexNumber(14, -11)
number_2 = ComplexNumber(-17, 3)
print(number_1 + number_2)
print(number_1 * number_2)

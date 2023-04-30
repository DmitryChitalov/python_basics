"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class MyComplex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return MyComplex(self.a + other.a, self.b + other.b)

    def __str__(self):
        return f"{self.a}+{self.b}i"

    def __mul__(self, other):
        return MyComplex(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)


number1 = MyComplex(1, 2)
number2 = MyComplex(2, 3)
print(f"Первое комплексное число: {number1}")
print(f"Второе комплексное число: {number2}")
print(f"Сумма чисел: {number1 + number2}")
print(f"Произведение чисел: {number1 * number2}")

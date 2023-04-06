class Myclass:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __add__(self, other):
        self.add1 = self.a + other.a + self.b + other.b
        return self.add1

    def __mul__(self, other):
        self.mul1 = self.a * other.a - self.b * other.b + self.a * other.b + other.a * self.b
        return self.mul1


a1 = Myclass(3, 4)
a2 = Myclass(5, 6)
print(a1 + a2)
print(a1 * a2)

"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

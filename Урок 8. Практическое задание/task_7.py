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
Я не смог понять что такое комплексные числа...
Если бы я понял что такое i, написал бы правиьно(((((
Формулы сложения и умножения подглядел.
"""
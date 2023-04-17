"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class ComplexNumb:
    def __init__(self, real_p, imagin_p):
        self.real_p = real_p
        self.imagin_p = imagin_p

    def __add__(self, other):
        return ComplexNumb(self.real_p + other.real_p, self.imagin_p + other.imagin_p)

    def __mul__(self, other):
        return ComplexNumb(self.real_p*other.real_p - self.imagin_p*other.imagin_p,
                             self.real_p*other.imagin_p + self.imagin_p*other.real_p)

    def __str__(self):
        return f"{self.real_p} + {self.imagin_p}i"


# Создаем экземпляры класса
a = ComplexNumb(2, 3)
b = ComplexNumb(3, 4)

# Складываем и умножаем комплексные числа
c = a + b
d = a * b

# Выводим результаты операций
print(c)
print(d)

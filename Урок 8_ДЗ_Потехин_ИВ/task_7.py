"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    # pзадаем комлексное число с частями: действительное \ мнимое
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # формируем метод сложения комплесных чисел
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    # формируем метод умножения комплесных чисел
    def __mul__(self, other):
        return ComplexNumber((self.real * other.real - self.imaginary * other.imaginary),
                             (self.real * other.imaginary + other.real * self.imaginary))

    def __str__(self):
        return f'{self.real}{"+" if self.imaginary > 0 else " "}{self.imaginary}i'


cn_1 = ComplexNumber(2, -1)
cn_2 = ComplexNumber(10, 3)
cn_3 = cn_1 + cn_2
cn_4 = cn_1 * cn_2
print(f'Сумма: {cn_3}')
print(f'Произведение: {cn_4}')

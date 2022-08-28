"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class MyComplexNumber:
    '''Комплексное число'''
    def __init__(self, compl):
        if isinstance(compl, complex):
            self.compl = compl
        else:
            raise ValueError('Введенное число должно быть комплексным!')
    def __add__(self, other):
        if isinstance(other, MyComplexNumber):
            real_part = self.compl.real + other.compl.real
            imag_part = self.compl.imag + other.compl.imag
            return real_part + imag_part * 1j
    def __mul__(self, other):
        if isinstance(other, MyComplexNumber):
            real_part = self.compl.real * other.compl.real \
                - self.compl.imag * other.compl.imag
            imag_part = self.compl.imag * other.compl.real \
                + self.compl.real * other.compl.imag
            return real_part + imag_part * 1j

val_1 = MyComplexNumber(10 + 5j)
val_2 = MyComplexNumber(15 + 4j)
print("Запускаем перегруженные методы")
print(val_1 + val_2)
print(val_1 * val_2)
print()
print("Проверяем перегруженные методы")
print((10 + 5j) + (15 + 4j))
print((10 + 5j) * (15 + 4j))

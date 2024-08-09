"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class OperComplexNumb:

    def __init__(self, comp_numb):
        self.comp_numb = comp_numb

    def __add__(self, other):
        res_sum = self.comp_numb + other.comp_numb
        return res_sum

    def __mul__(self, other):
        res_mul = self.comp_numb * other.comp_numb
        return res_mul

my_comp_numb1 = OperComplexNumb(5 + 6j)
my_comp_numb2 = OperComplexNumb(7 + 8j)
print(my_comp_numb1 + my_comp_numb2)
print(my_comp_numb1 * my_comp_numb2)
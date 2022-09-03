"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class OperationComplNum:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __add__(self, numm):
        print(f"\nСумма равна:")
        return f"x = {self.a + numm.a} + {self.b + numm.b} * i"

    def __mul__(self, numm):
        print(f"\nПроизведение равно:")
        return f"x = {self.a * numm.a - (self.b * numm.b)} + {self.b * numm.a} * i"


a_1 = OperationComplNum(1, -2)
b_2 = OperationComplNum(3, 4)
print(a_1 + b_2)
print(a_1 * b_2)
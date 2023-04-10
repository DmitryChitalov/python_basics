"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumbers:
    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value

    def __add__(self, other):
        return ComplexNumbers(self.first_value + other.first_value, self.second_value + other.second_value)

    def __mul__(self, other):
        return ComplexNumbers(self.first_value * other.first_value - self.second_value * other.second_value,
                              self.first_value * other.second_value + self.second_value * other.first_value)


first_complex_numbers = ComplexNumbers(44, 55)
second_complex_numbers = ComplexNumbers(22, 33)

result_addition = first_complex_numbers + second_complex_numbers
result_multiplication = first_complex_numbers * second_complex_numbers

print(f'Результат сложения: {result_addition.first_value}, {result_addition.second_value}')
print(f'Результат умножения: {result_multiplication.first_value}, {result_multiplication.second_value}')

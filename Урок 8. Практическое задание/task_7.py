"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class ComplexusNumbers:

    def __init__(self, first_real_number, second_real_number):
        self.first_real_number = first_real_number
        self.second_real_number = second_real_number

    def __add__(self, auxiliary):
        return ComplexusNumbers(self.first_real_number + auxiliary.first_real_number, self.second_real_number + auxiliary.second_real_number)

    def __mul__(self, auxiliary):
        return ComplexusNumbers((self.first_real_number * auxiliary.first_real_number - self.second_real_number * auxiliary.second_real_number),
                             (self.first_real_number * auxiliary.second_real_number + auxiliary.first_real_number * self.second_real_number))

    def __str__(self):
        return f"{self.first_real_number}{'+' if self.second_real_number > 0 else ''}{self.second_real_number}i"

first_complexus_numbers = ComplexusNumbers(114, 48)
second_complexus_numbers = ComplexusNumbers(55, 115)

result_addition = first_complexus_numbers + second_complexus_numbers
result_multiplication = first_complexus_numbers * second_complexus_numbers

print(f'Результат сложения: {result_addition.first_real_number}, {result_addition.second_real_number}')
print(f'Результат умножения: {result_multiplication.first_real_number}, {result_multiplication.second_real_number}')

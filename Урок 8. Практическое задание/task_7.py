"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
import re


class Complexus:

    def __init__(self, comlex_number):
        if comlex_number[0] == '-':
            comlex_number = comlex_number[1:-1]
            if comlex_number.find('-') != -1:
                self.first = int("-" + re.split('[- ]', comlex_number)[0])
                self.second = int('-' + re.split('[- ]', comlex_number)[1].replace('i', ''))
            else:
                self.first = int("-" + re.split('[+ ]', comlex_number)[0])
                self.second = int('-' + re.split('[+ ]', comlex_number)[1].replace('i', ''))
        else:
            if comlex_number.find('-') != -1:
                self.first = int(re.split('[- ]', comlex_number)[0])
                self.second = int('-' + re.split('[- ]', comlex_number)[1].replace('i', ''))
            else:
                self.first = int(re.split('[+ ]', comlex_number)[0])
                self.second = int('-' + re.split('[+ ]', comlex_number)[1].replace('i', ''))

    def __str__(self):
        return f"{self.first}{self.second}i"

    def __add__(self, other):
        a = self.first + other.first
        b = self.second + other.second
        return Complexus(f"{a}{b}i")

    def __mul__(self, other):
        a = (self.first * other.first) - (self.second * other.second)
        b = (self.first * other.second) + (self.second * other.first)
        return Complexus(f"{a}{b}i")

c1 = Complexus('5-7i')
c2 = Complexus('4-5i')
print(f"sum of c1 and  c2 will be {c1 + c2}")
print(f"multiplication of c1 and c2 will be {c1 * c2}")


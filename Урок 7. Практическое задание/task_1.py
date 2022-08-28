"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    def __init__(self, my_lst):
        self.my_lst = my_lst

    def __str__(self):
        new_view = [str(el).strip('[]').replace(',', '')
                    for el in self.my_lst]
        return "\n".join(new_view)

    def __add__(self, other):
        for n in range(len(self.my_lst)):
            for m in range(len(self.my_lst)):
                self.my_lst[n][m] = int(self.my_lst[n][m]) + int(other.my_lst[n][m])
        return Matrix(self.my_lst)


a = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(f"{a.__dict__}\n{b.__dict__}")

print(f"Значения матрицы а:\n{a}")
print(f"Значения матрицы b:\n{b}")

c = a + b
print(f"Сумма матриц а и b:\n{c}")


class Matrix:
    def __init__(self, my_lst):
        self.my_lst = my_lst
    def __str__(self):
        new_view = [str(el).strip('[]').replace(',', '')
                    for el in self.my_lst]
        return "\n".join(new_view)
    def __add__(self, other):
        for n in range(len(self.my_lst)):
            for m in range(len(self.my_lst)):
                self.my_lst[n][m] = int(self.my_lst[n][m]) + int(other.my_lst[n][m])
        return Matrix(self.my_lst)


a = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(f"{a.__dict__}\n{b.__dict__}")

print(f"Значения матрицы а:\n{a}")
print(f"Значения матрицы b:\n{b}")

c = a + b
print(f"Сумма матриц а и b:\n{c}")
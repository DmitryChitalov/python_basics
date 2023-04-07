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
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        return "\n".join([" ".join([str(el) for el in row]) for row in self.matrix_list])

    def __add__(self, other):
        if len(self.matrix_list) != len(other.matrix_list) or len(self.matrix_list[0]) != len(other.matrix_list[0]):
            raise ValueError("Размер матриц должен быть одинаков")
        result = []
        for elem in range(len(self.matrix_list)):
            row = []
            for element in range(len(self.matrix_list[0])):
                row.append(self.matrix_list[elem][element] + other.matrix_list[elem][element])
            result.append(row)
        return Matrix(result)


matrix1 = Matrix([[5, 45, 4], [13, 7, 9], [-2, 4, 11]])
matrix2 = Matrix([[-1, 3, 9], [4, 4, 3], [7, 0, 9]])

print(f'Значения первой матрицы:\n{matrix1}')
print(f'Значения второй матрицы:\n{matrix2}')

matrix_sum = matrix1 + matrix2
print(f'Результат сложения:\n{matrix_sum}')

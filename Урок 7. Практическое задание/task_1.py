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
    def __init__(self, my_matrix: list):
        self.matrix = my_matrix

    def __str__(self):
        tmp_str = ""
        tmp_len = len(self.matrix)
        i = 0
        for row in self.matrix:
            if i < tmp_len - 1:
                tmp_str = tmp_str + f"{row} \n"
                i += 1
            else:
                tmp_str = tmp_str + f"{row}"
        return tmp_str

    def __add__(self, other):
        new_matrix = []
        row_count = len(self.matrix)
        col_count = len(self.matrix[0])
        i = 0
        while i < row_count:
            first_row_for_sum = self.matrix[i]
            second_row_for_sum = other.matrix[i]
            sum_row = []
            j = 0
            while j < col_count:
                sum_row.append(first_row_for_sum[j] + second_row_for_sum[j])
                j += 1

            new_matrix.append(sum_row)
            i += 1

        return Matrix(new_matrix)


matrix1 = Matrix([[1, 2, 3], [1, 2, 6], [1, 2, 3]])
matrix2 = Matrix([[3, 2, 1], [3, 2, 1], [3, 2, 1]])
print("Первая матрица:")
print(matrix1)
print("*****")

print("Вторая матрица:")
print(matrix2)
print("*****")

print("Сумма введенных матриц:")
print(matrix1 + matrix2)
print("*****")
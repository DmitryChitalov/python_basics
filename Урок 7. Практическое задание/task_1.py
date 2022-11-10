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
    """
    класс Matrix (матрица)
    """
    def __init__(self, matrix):
        self.matrix = matrix
        if not self.__check_matrix():
            raise AttributeError("attribute matrix not a valid matrix!")

    def __add__(self, other):
        if not self.eq_size(other):
            raise AttributeError("matrix size not equals!")
        result = []
        o_iter = iter(other.matrix)
        for s_row in self.matrix:
            o_r_iter = iter(next(o_iter))
            r_row = [s_cell + next(o_r_iter) for s_cell in s_row]
            result.append(list(r_row))
        return Matrix(result)

    def __str__(self) -> str:
        return "\n".join(map(lambda row: " ".join([str(cell) for cell in row]), self.matrix))

    def eq_size(self, other):
        """
        Сравнивает размерность матриц
        """
        return len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0])

    def __check_matrix(self):
        """
        проверяет валидность матрицы
        """
        if not isinstance(self.matrix, list):
            return False
        if len(self.matrix) < 2:
            return False
        row_size = -1
        for row in list(self.matrix):
            if len(row) == 0:
                return False
            if row_size == -1:
                row_size = len(row)
                continue
            if len(row) != row_size:
                return False
        return True


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m1)
print()
m2 = Matrix([[2, 4, 6], [3, 5, 7], [4, 6, 8]])
print(m2)
print()
m1_m2 = m1 + m2
print(m1_m2)
print()
m3 = Matrix([[1, 2], [4, 5]])
print(m3)
m1_m3 = m1 + m3  # exception called AttributeError("matrix size not equals!")

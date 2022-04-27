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

from typing import List


class Matrix:
    __elements:List[List[int]] = None
    __rows_count = 0
    __column_count = 0

    def __init__(self, *argv:List[int]) -> None:
        self.__elements = list(argv)
        self.__rows_count = len(self.__elements)
        #проверяем что матрица корректная по размерности
        if self.__rows_count > 0:
            #Берём количество элементов первой строки матрицы и сравниваем с количеством элементов в каждой строке матрицы
            self.__column_count = len(self.__elements[0])
            for row in self.__elements:
                if self.__column_count != len(row):
                    raise ValueError("Matrix has different column count in rows.")
        else:
            raise ValueError("Matrix has empty rows.")

    def __str__(self) -> str:
        result = ""
        for row in self.__elements:
            for el in row:
                result += f"{el} "
            result += "\n"
        return result

    def __add__(self, matrix):
        if type(matrix) is Matrix:
            cast_matrix:Matrix = matrix
            if self.row_count != cast_matrix.row_count or self.column_count != cast_matrix.column_count:
                raise ValueError("You can't added matrix with different row or columns count.")
            else:
                result_elements = []
                ndx = 0
                while ndx < len(self.elements):
                    c_ndx = 0
                    result_row = []
                    while c_ndx < len(self.elements[ndx]):
                        result_row.append(self.elements[ndx][c_ndx] + cast_matrix.elements[ndx][c_ndx])
                        c_ndx += 1
                    
                    result_elements.append(result_row)
                    ndx += 1
                
                return Matrix(*result_elements)
        else:
            raise ValueError("You can added only other matrix.")


    @property
    def elements(self):
        return self.__elements

    @property
    def row_count(self):
        return self.__rows_count

    @property
    def column_count(self):
        return self.__column_count

matrix_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
matrix_2 = Matrix([3, 2, 1], [6, 5, 4], [9, 8, 7])
matrix_3:Matrix = matrix_1 + matrix_2
print(matrix_3)
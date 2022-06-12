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
    def __init__(self, ar_of_ar):
        len_of_matrix = len(ar_of_ar[0])
        for ar in ar_of_ar:
            if not len(ar) == len_of_matrix:
                print(f'Passed an array of arrays of different lengths.')
                raise ValueError
        self._data = ar_of_ar

    def __str__(self):
        result = f'Matrix\n(\t' + f'\t)\n(\t'.join(
            f', '.join(str(x) for x in line) for line in self._data) + f'\t);'
        return result

    def __add__(self, other):
        len_of_matrix = len(self._data[0])
        hig_of_matrix = len(self._data)
        if not (len_of_matrix == len(other._data[0]) and hig_of_matrix == len(
                other._data)):
            print("Matrices of the same size are accepted for addition.")
            raise ValueError
        result = [[self._data[y][x] + other._data[y][x] for x in
                   range(len_of_matrix)]
                  for y in range(hig_of_matrix)]
        return Matrix(result)


if __name__ == '__main__':
    list_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    list_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print(list_1)
    print(list_2)

    result_1 = list_1 + list_2
    print(result_1)

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
        print_list = ""
        for el_list in self.matrix_list:
            print_list = print_list + " ".join(map(str, el_list)) + "\n"
        return print_list

    def __add__(self, other):
        sum_matrix = []
        for el1, el2 in zip(self.matrix_list, other.matrix_list):
            sum_ind = []
            for ind1, ind2 in zip(el1, el2):
                sum_ind.append(int(ind1) + int(ind2))
            sum_matrix.append(sum_ind)
        return Matrix(sum_matrix)


def input_list():
    inp_list = []
    for el in range(0, 3):
        inp_list.append(input("Введите элементы строки матрицы через пробел: ").split())
    return inp_list


print_matrix_1 = Matrix(input_list())
print_matrix_2 = Matrix(input_list())
print(f"Первая матрица: \n{print_matrix_1}")
print(f"Вторая матрица: \n{print_matrix_2}")
print(f"Сумма матриц: \n{print_matrix_1 + print_matrix_2}")

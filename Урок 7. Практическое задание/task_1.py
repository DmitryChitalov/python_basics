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
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        try:
            __matrix = ""

            for el in self.arg:
                __matrix += ' '.join([str(e) for e in el]) + '\n'
            return f"{__matrix}"
        except BaseException as e:
            print(f"General error: {e}")

    def __add__(self, other):
        try:
            out_list = []
            for i, el in enumerate(self.arg, 0):
                int_list = []
                for j, e in enumerate(el, 0):
                    int_list.append(int(e + other.arg[i][j]))
                out_list.append(int_list)

            return f"Сумма матриц: \n{out_list}"

        except BaseException as e:
            print(f"General error: {e}")


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])

print(matrix_1)
print(matrix_2)

print(matrix_1 + matrix_2)

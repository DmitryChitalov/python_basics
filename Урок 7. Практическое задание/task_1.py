"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init()__),который должен принимать данные (список списков) для
формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы
в привычном виде.

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
            for m, el in enumerate(self.arg, 0):
                int_list = []
                for n, e in enumerate(el, 0):
                    int_list.append(int(e + other.arg[m][n]))
                out_list.append(int_list)

            result_matrix = ""
            for el in out_list:
                result_matrix += ' '.join([str(e) for e in el]) + '\n'
            return f"Сумма матриц: \n{result_matrix}"

        except BaseException as e:
            print(f"General error: {e}")


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Первая матрица: \n{matrix1}")

matrix2 = Matrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
print(f"Вторая матрица: \n{matrix2}")

print(matrix1 + matrix2)

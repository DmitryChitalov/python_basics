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
    result = []

    def __init__(self, list):
        self.list = list

    def __str__(self):
        matrx_str = ""
        for i in range(len(self.list)):
            for j in range(len(self.list[i])):
                matrx_str = matrx_str + f"{self.list[i][j]} "
            matrx_str = matrx_str + "\n"
        return matrx_str

    def __add__(self, other):

        matrx_result = ""
        for i in range(len(self.list)):
            for j in range(len(self.list[i])):
                matrx_result = matrx_result + f"{self.list[i][j] + other.list[i][j]} "
            matrx_result = matrx_result + "\n"
        return matrx_result


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print(f"Cумма матриц: \n {a + b}")

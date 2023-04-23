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

    def __init__(self, in_matrlist):
        self.matrix = in_matrlist

    def __str__(self):
        res = "\n"
        for i1 in range(len(self.matrix)):
            tmp_list = self.matrix[i1]
            for el in tmp_list:
                res += f"{el} "
            res += "\n"
        return res

    def __add__(self, other):
        result = []
        for i1 in range(len(self.matrix)):
            tmp_list1 = self.matrix[i1]
            tmp_list2 = other.matrix[i1]
            tmp_list3 = []
            for i2 in range(len(tmp_list1)):
                tmp_list3.append(tmp_list1[i2] + tmp_list2[i2])
            result.append(tmp_list3)
        return Matrix(result)


obj_m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
obj_m2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
obj_m3 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
obj_m4 = Matrix([[1, 1, 1, 1], [1, 1, 1, 1]])
print(f"Матрица 1: {obj_m1}")
print(f"Матрица 2: {obj_m2}")
print(f"Сумма матриц 1 и 2: {obj_m1 + obj_m2}")
print(f"Матрица 3: {obj_m3}")
print(f"Матрица 4: {obj_m4}")
print(f"Сумма матриц 3 и 4: {obj_m3 + obj_m4}")

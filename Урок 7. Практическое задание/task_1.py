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
class Matrix():

    def __init__(self, mtrx):
        self.mtrx = mtrx

    def __str__(self):
        res = ''
        for item in self.mtrx:
            for el in item:
                res += f'{el} '
            res += '\n'
        return res
    
    def __add__(self, matrix_object):
        mtrx = []
        for item_a, item_b in zip(self.mtrx, matrix_object.mtrx):
            new_item = []
            for el_a, el_b in zip(item_a, item_b):
                new_item.append(int(el_a) + int(el_b))
            mtrx.append(new_item)
        return(Matrix(mtrx))

test_mtrx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m1 = Matrix(test_mtrx)
m2 = Matrix(test_mtrx)
m3 = m1 + m2
print(m3)
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
    '''Матрица'''
    elements = []
    __complete_lines = 0
    def __init__(self, elements):
        for el in elements:
            if isinstance(el, list) and len(el) == 3:
                self.__complete_lines += 1
        if self.__complete_lines == 3:
            self.elements = elements
    def __str__(self):
        return  f'{" ".join(str(item) for item in self.elements[0])} \n' \
                f'{" ".join(str(item) for item in self.elements[1])} \n' \
                f'{" ".join(str(item) for item in self.elements[2])} \n'
    def __add__(self, other_matrix):
        new_elements = []
        i = 0
        for line in other_matrix.elements:
            new_line = []
            for item in line:
                sum_of = item + self.elements[i][line.index(item)]
                new_line.append(sum_of)
            i += 1
            new_elements.append(new_line)
        return Matrix(new_elements)

m1 = Matrix([[1,2,3], [4,5,6], [7,8,9]])
m2 = Matrix([[1,2,3], [4,5,6], [7,8,9]])
print(
    f'Первая матрица: \n'
    f'{m1}'
    f'Вторая матрица: \n'
    f'{m2}'
    f'Сумма матриц: \n'
    f'{m1 + m2}'
)

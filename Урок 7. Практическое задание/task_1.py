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
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __str__(self):
        max_len = 1  
        copy_matrix = self.matrix.copy()  
        for i in range(len(copy_matrix)):
            copy_matrix[i] = list(map(str, copy_matrix[i]))  # приведение к строке
            # присвоение нового значения наибольшей длинне, если текущее число длиннее предыдущих
            max_len = len(max(copy_matrix[i], key=len)) if max_len < len(max(copy_matrix[i], key=len)) else max_len

        # формирование строки для вывода
        string = ''
        for i in range(len(copy_matrix)):
            for j in range(len(copy_matrix[i])):
                copy_matrix[i][j] = copy_matrix[i][j].ljust(max_len)  
            string += ' '.join(copy_matrix[i])  # добавление строки матрицы к строке для вывода
            string += '\n' if i != len(copy_matrix) - 1 else ''
        return string

    def __add__(self, other):
        result = []  
        for i in range(len(self.matrix)):
            result_row = []  # список для строки
            for j in range(len(self.matrix[i])):
                result_el = self.matrix[i][j] + other.matrix[i][j]  # вычисление элемента
                result_row.append(result_el)  # добавление в результирующую строку матрицы
            result.append(result_row)  # добавление в результирующий список
        return Matrix(result)  

m = Matrix([[2, 5, 7], [10, 8, 3], [6, 13, 1]])
n = Matrix([[9, 6, 8], [7, 2, 11], [5, 4, 14]])

print(m)
print()
print(n)
print()
print(m + n)

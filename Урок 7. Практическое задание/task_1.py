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
        max_len = 1  # начальное значение для определения наибольшей длинны числа в матрице
        copy_matrix = self.matrix.copy()  # создание копии матрицы для дальнейших преобразований
        for i in range(len(copy_matrix)):
            copy_matrix[i] = list(map(str, copy_matrix[i]))  # приведенеие всех чисел в матрице к строке
            # присвоение нового значения наибольшей длинне, если текущее число длинне предыдущих
            max_len = len(max(copy_matrix[i], key=len)) if max_len < len(max(copy_matrix[i], key=len)) else max_len

        # формирование строки для вывода
        string = ''
        for i in range(len(copy_matrix)):
            for j in range(len(copy_matrix[i])):
                copy_matrix[i][j] = copy_matrix[i][j].ljust(max_len)  # форматирование чисел одинаковой длины
            string += ' '.join(copy_matrix[i])  # добавление строки матрицы к строке для вывода
            # добавление переноса строки, если эта строка не последняя
            string += '\n' if i != len(copy_matrix) - 1 else ''
        return string

    def __add__(self, other):
        result = []  # список для формированеи результата
        for i in range(len(self.matrix)):
            result_row = []  # список для формирования строки матрицы
            for j in range(len(self.matrix[i])):
                result_el = self.matrix[i][j] + other.matrix[i][j]  # вычисление элемента
                result_row.append(result_el)  # добавление в результирующую строку матрицы
            result.append(result_row)  # добавление в результирующий список
        return Matrix(result)  # возврат объекта класса Matrix


# проверка
m = Matrix([[3, 24, 22], [23444, 4, 333], [44, 33, 1234]])
n = Matrix([[97, 76, 78], [76556, 6, 667], [44, 33, 4321]])

print(m)
print()
print(n)
print()
print(m + n)

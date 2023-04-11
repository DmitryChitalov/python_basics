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
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, addition_input):
        result = ''
        for line_1, line_2 in zip(self.input, addition_input.input):
            resulting_line = [x + y for x, y in zip(line_1, line_2)]
            result += ' '.join(map(str, resulting_line)) + '\n'
        return result

first_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
second_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Первая матрица: \n{first_matrix}")
print(f"Вторая матрица: \n{second_matrix}")
sum_of_matrices = first_matrix + second_matrix
print(f"Сумма матриц: \n{sum_of_matrices}")

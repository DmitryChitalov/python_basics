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
    """Класс Матрица"""

    def __init__(self, lst: list):
        """Инициализация параметров"""
        self.matrix = lst

    def __str__(self):
        """Вывод матрицы"""
        return_mrx = []
        for elems in self.matrix:
            return_mrx.append(str(elems).replace(',', '')
                .replace('[', '').replace(']', '') +'\n')

        mrx = ''.join(return_mrx)

        return f"Матрица:\n{mrx}"

    def __add__(self, another):
        """Метод сложения матриц"""
        new_lst = []
        return_mrx = []

        for elems in range(len(self.matrix)):
            for elem in range(len(self.matrix[elems])):
                new_lst.append(self.matrix[elems][elem] + another.matrix[elems][elem])

        counter = 0
        counter_list = 0
        counts = ([len(i) for i in [j for j in self.matrix]])

        for elem in new_lst:
            return_mrx.append(str(elem) + ' ')
            counter += 1
            if counter == counts[counter_list]:
                counter = 0
                counter_list += 1
                return_mrx.append('\n')
        mrx = ''.join(return_mrx)

        return f"Сумма Матриц:\n{mrx}"


matrx_1 = Matrix([[1, 2, 3, 3], [4, 5, 6], [7, 8, 9]])
matrx_2 = Matrix([[1, 2, 3, 4], [4, 5, 6], [7, 8, 9]])

print(matrx_1)
print(matrx_2)

print(matrx_1 + matrx_2)

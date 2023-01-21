"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем 
с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:
    def __init__(self, *args):
        self.my_list = list(args)
    
    def __str__(self):
        result_with =  '\n'.join(map(str, self.my_list))
        result_without = result_with.replace(',', '').replace('[', '').replace(']', '')
        return result_without
    
    def __add__(self, other):
        new_result = []
        str_sum = []
        for x in range(len(self.my_list)):
            for y in range(len(self.my_list[x])):
                str_sum.append(self.my_list[x][y] + other.my_list[x][y])
            new_result.append(str_sum)
            str_sum = []
        return Matrix('\n'.join(map(str, new_result)))
        


matrix_obj_1 = Matrix([31, 32], [37, 43], [51, 86])
print(matrix_obj_1)

print()

matrix_obj_2 = Matrix([3, 5, 32], [2, 4, 6], [-1, 64, -8])
print(matrix_obj_2)

print()

matrix_obj_3 = Matrix([3, 5, 8, 3], [8, 3, 7, 1])
print(matrix_obj_3)

print()

print(matrix_obj_1 + matrix_obj_2)


class Matrix:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return '\n'.join(' '.join([str(i) for i in el]) for el in self.args)

    def __add__(self, other):
        if len(self.args) != len(other.args):
            return 'Сложение невозможно, т.к. матрицы не равны'
        for el_1, el_2 in zip(self.args, other.args):
            if len(el_1) != len(el_2):
                return 'Сложение невозможно, т.к. матрицы не равны'
        res = [[self.args[i][j] + other.args[i][j] for j in range(len(self.args[0]))] for i in range(len(self.args))]
        return Matrix(res)

mat_1 = Matrix([31, 32],[37, 43], [51,86])
mat_2 = Matrix([3, 5, 32], [2, 4, 6], [-1, 64, -8])
mat_3 = Matrix([3, 5, 8, 3], [8, 3, 7, 1])
mat_4 = Matrix([9, 8], [3, -3], [-11, -46])

print(mat_1 + mat_2)
print(mat_1 + mat_4)


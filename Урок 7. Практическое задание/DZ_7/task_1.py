
class matrix(object):

    def __init__(self, matrix):
         self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, matrix_2):
        res = []
        for i in range(len(self.matrix)):
            res.append([])
            for j in range(len(self.matrix[i])):
                new_matrix = self.matrix[i][j] + matrix_2.matrix[i][j]
                res[i].append(new_matrix)

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in res]))


m_1 = matrix([[1, 2, 3], [1, 2, 3]])
m_2 = matrix([[1, 2, 3], [1, 2, 3]])

print(m_1)
print(m_1.__add__(m_2))
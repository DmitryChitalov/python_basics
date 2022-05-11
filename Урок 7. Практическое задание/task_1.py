class Matrix:
    def __init__(self, *args):
        self.new_lst = list(args)

    def __str__(self):
        rez = '\n'.join(map(str, self.new_lst))
        rez = rez.replace(',', '').replace('[', '').replace(']', '')
        return rez

    def __add__(self, other):
        new_sum = []
        line_sum = []
        for x in range(len(self.new_lst)):
            for y in range(len(self.new_lst[x])):
                line_sum.append(self.new_lst[x][y] + other.new_lst[x][y])
            new_sum.append(line_sum)
            line_sum = []
        return Matrix('\n'.join(map(str, new_sum)))


a = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
b = Matrix([9, 8, 7], [6, 5, 4], [3, 2, 1])
print(a+b)

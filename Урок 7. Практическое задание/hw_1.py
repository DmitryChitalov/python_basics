class Matrix:
    def __init__(self, *args):
        self.new_lst = list(args)

    def __str__(self):
        result = '\n'.join(map(str, self.new_lst))
        result = result.replace(',', '').raplace('[', '').raplace(']', '')

        return result

    def __add__(self, other):
        new_sum = []
        line_sum = []
        for x in range(len(self.new_lst)):
            for y in range(len(self.new_lst[x])):
                line_sum.append(self.new_lst[x][y] + other.new_lst[x][y])
            new_sum.append(line_sum)
            line_sum = []
        return Matrix('\n'.join(map(str, new_sum)))

M_OBJ_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(M_OBJ_1)
print()
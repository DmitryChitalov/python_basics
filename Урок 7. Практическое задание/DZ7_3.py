class Cell:
    def __init__(self, N):
        self.N = N

    def __add__(self, other):
        add_cell = []
        total_cell = self.N + other.N
        i = 0
        while i < total_cell:
            add_cell.append('*')
            i += 1
        return add_cell

    def __sub__(self, other):
        if (self.N - other.N) > 0:
            sub_cell = []
            total_cell = self.N - other.N
            i = 0
            while i < total_cell:
                sub_cell.append('*')
                i += 1
        else:
            "Вычитание невозможно"
        return sub_cell

    def __mul__(self, other):
        mul_cell = []
        total_cell = self.N * other.N
        i = 0
        while i < total_cell:
            mul_cell.append('*')
            i += 1
        return mul_cell

    def __truediv__(self, other):
        div_cell = []
        total_cell = self.N // other.N
        i = 0
        while i < total_cell:
            div_cell.append('*')
            i += 1
        return div_cell
    def make_order(self, el):
        cell_order = ''
        for i in range(int(self.N / el)):
            cell_order += f'{"*" * el} \\n '
        cell_order += f'{"*" * (self.N % el)}'
        return cell_order

cell_1 = Cell(11)
cell_2 = Cell(3)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(2))

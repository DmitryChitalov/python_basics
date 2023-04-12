class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        result = self.cells - other.cells
        if result > 0:
            return Cell(result)
        else:
            print("Разность количества ячеек двух клеток меньше или равна 0")
            return None

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, cells_per_row):
        rows = self.cells // cells_per_row
        remainder = self.cells % cells_per_row
        return ('*' * cells_per_row + '\n') * rows + '*' * remainder

cell1 = Cell(10)
cell2 = Cell(3)

print((cell1 + cell2).make_order(5))
print((cell1 - cell2).make_order(5))
print((cell1 * cell2).make_order(5))
print((cell1 / cell2).make_order(5))

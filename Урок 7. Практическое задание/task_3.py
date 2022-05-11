class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'({self.quantity})'

    def __add__(self, other):
        return f'Сумма клеток = {str(Cell(self.quantity + other.quantity))}'

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return f'Разность клеток = {Cell(int(self.quantity - other.quantity))}'
        return f'Разность отрицательна, поэтому операция не выполняется'

    def __mul__(self, other):
        return f'Умножение клеток = {Cell(int(self.quantity * other.quantity))}'

    def __truediv__(self, other):
        return f'Деление клеток = {Cell(round(self.quantity // other.quantity))}'

    def make_order(self, cells_count):
        row = ''
        for _ in range(int(self.quantity / cells_count)):
            row += f'{"*" * cells_count}\\n '
        row += f'{"*" * (self.quantity % cells_count)}'
        return row


print("Создаем объекты клеток")
cell1 = Cell(40)
cell2 = Cell(46)

cell3 = Cell(11)
cell4 = Cell(48)

print()

print("Сложение")
print(cell1 + cell4)

print()

print("Вычитание")
print(cell1 - cell3)
print(cell2 - cell4)

print()

print("Умножение")
print(cell3 * cell1)

print()

print("Деление")
print(cell4 / cell1)

print()

print("Организация по рядам")
print(cell1.make_order(9))
print(cell2.make_order(15))

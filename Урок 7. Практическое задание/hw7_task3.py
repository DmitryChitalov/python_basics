class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f"Сумма клеток: {self.quantity + other.quantity}"

    def __sub__(self, other):
        sub_cell = self.quantity - other.quantity
        if sub_cell > 0:
            return f"Разность клеток: {sub_cell}"
        else:
            return f"Клеток больше нет"

    def __mul__(self, other):
        return f"Произведение клеток: {self.quantity * other.quantity}"

    def __truediv__(self, other):
        return f"Деление клеток: {self.quantity // other.quantity}"


c = Cell(10)
c2 = Cell(6)
print(c + c2)
print(c - c2)
print(c * c2)
print(c / c2)

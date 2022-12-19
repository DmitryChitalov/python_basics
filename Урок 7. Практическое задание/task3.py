class Cell:

    def __init__(self, amount):
        self.amount = int(amount)

    def __add__(self, other):
        return f"Сумма клеток: {self.amount + other.amount}"

    def __sub__(self, other):
        if self.amount > other.amount:
            return f"Разность клеток: {self.amount - other.amount}"
        else:
            return "Вычетание не возможно, т.к. разность < 0"

    def __mul__(self, other):
        return f"Произведение клеток: {self.amount * other.amount}"

    def __truediv__(self, other):
        return f"Деление клеток: {self.amount // other.amount}"

    def make_order(self, amount_cell):
        result = ''
        for el in range(self.amount // amount_cell):
            for i in range(amount_cell):
                result += "*"
            result += "\n"
        for el in range(self.amount % amount_cell):
            result += "*"
        return result

a = Cell(15)
b = Cell(20)

print(a + b)
print(a - b)
print(b - a)
print(a * b)
print(a / b)
print(b / a)
print(a.make_order(6))

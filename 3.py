"""
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
    - сложение (​__add__())​
    - вычитание (​__sub__())​
    - умножение (​__mul__())​
    - деление (​__truediv__())​.
Данные методы должны применяться т​олько к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение.​ Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание.​ Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение.​ Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление.​ Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод ​make_order(),​ принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *​****\n*****\n*****.​.. , где количество ячеек между \​n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() ​вернет строку: *​****\n*****\n**.​
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() ​вернет строку: *​****\n*****\n*****.​
"""


class Cell:
    __count: int

    def __init__(self, count: int):
        assert count > 0, "Количество ячеек должно быть больше 0"
        self.__count = count

    def __add__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count + other.count
        return Cell(value)

    def __sub__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count - other.count
        assert value > 0, "Разность ячеек меньше 0"
        return Cell(value)

    def __mul__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count * other.count
        return Cell(value)

    def __truediv__(self, other: 'Cell'):
        self.validate_item(other)
        value = round(self.count / self.count)
        return Cell(value)

    def __str__(self):
        return str(self.__count)

    def validate_item(self, other):
        assert isinstance(other, self.__class__), "Операции допустимы только между клетками"

    @property
    def count(self) -> int:
        return self.__count

    @staticmethod
    def make_order(cell_object: 'Cell', count_per_row: int) -> str:
        items = '*' * cell_object.count
        chunks = [
            items[idx:idx + count_per_row]
            for idx in range(0, len(items), count_per_row)
        ]

        return '\n'.join(chunks)


first = Cell(3)
second = Cell(2)
huge = Cell(12)

print(first + second)  # 3 + 2 = 5
print(first - second)  # 3 - 2 = 1
print(first * second)  # 3 * 2 = 6
print(first / second)  # 3 / 2 = 1 (округление)

print(Cell.make_order(huge, 5))
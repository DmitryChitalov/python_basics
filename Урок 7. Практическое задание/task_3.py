"""
Реализовать программу работы с органическими клетками, состоящими
из ячеек. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству ячеек клетки
(целое число). В классе должны быть реализованы методы перегрузки
арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы должны
применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление
клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей
клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять
только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей
клетки определяется как произведение количества ячеек этих
двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей
клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий
экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек
в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, count: int):
        self._count = count

    def __add__(self, other: "Cell") -> "Cell":
        return Cell(self._count + other._count)

    def __sub__(self, other: "Cell") -> "Cell":
        if self._count > other._count:
            return Cell(self._count - other._count)

        # raise ValueError(f"{self._count} - {other._count}: impossible operation")
        print(f"{self._count} - {other._count}: impossible operation")

    def __mul__(self, other: "Cell") -> "Cell":
        return Cell(self._count * other._count)

    def __truediv__(self, other: "Cell") -> "Cell":
        return Cell(self._count // other._count)

    def make_order(self, per_row: int) -> str:
        rows, tail = self._count // per_row, self._count % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self) -> str:
        return f"Клетка состоит из {self._count} ячеек"


if __name__ == '__main__':
    c1 = Cell(17)
    print(c1)
    c2 = Cell(13)
    print(c2)

    print(c1 + c2)
    print(c1 - c2)
    print(c2 - c1)
    print(c2 - c2)
    print(c1 * c2)
    print(c1 / c2)
    print((c1 * c2).make_order(23))

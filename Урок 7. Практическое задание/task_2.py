'''
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, name: str, size: int):
        self.size = size
        super().__init__(name)

    @property
    def fabric_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, name: str, height: int):
        self.height = height
        super().__init__(name)

    @property
    def fabric_consumption(self):
        return round(2 * self.height + 0.3, 2)


if __name__ == '__main__':
    sewing_coat = Coat('Пошив пальто, размер: ', 58)
    sewing_suit = Suit('Пошив костюма, рост: ', 185)
    print(f'Расход ткани на пошив пальто: {sewing_coat.fabric_consumption}')
    print(f'Расход ткани на пошив костюма: {sewing_suit.fabric_consumption}')
    print(f'Общий расход ткани: {sewing_coat.fabric_consumption + sewing_suit.fabric_consumption}')
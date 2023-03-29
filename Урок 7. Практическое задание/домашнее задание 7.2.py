# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod
# расчет в метрах

class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes): # дочерний класс пальто
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property # к методу как к атрибуту объекта
    def consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes): # дочерний класс костюм
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def consumption(self):
        return round((2 * self.height + 0.3)/100, 2) # делим на 100 чтобы получить метры


coat = Coat("Пальто", 52)
suit = Suit("Костюм", 170)

print(coat.name, "расход ткани:", coat.consumption, "метров")
print(suit.name, "расход ткани:", suit.consumption, "метров")
print("Общий расход ткани:", round(coat.consumption + suit.consumption, 2), "метров")

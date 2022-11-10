"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""


from abc import ABC, abstractmethod


class FabricConsumption(ABC):
    """
    Класс подсчет расхода ткани
    """
    @abstractmethod
    def calc_consumption(self):
        """
        Метод подсчета расхода ткани
        """


class Clothes(FabricConsumption):
    """
    Единственный класс этого проекта — одежда (класс Clothes)
    """

    __AVAILABLE_TYPES = {"coat", "suit"}

    def __init__(self, c_type, c_param) -> None:
        super().__init__()
        self.clothes_type = c_type
        self.clothes_param = c_param

    @property
    def clothes_type(self):
        """
        возвращает тип одежды
        """
        return self.__clothes_type

    @clothes_type.setter
    def clothes_type(self, clothes_type):
        if clothes_type not in self.__AVAILABLE_TYPES:
            raise AttributeError(f"unknown clothes type '{clothes_type}'")
        self.__clothes_type = clothes_type

    @property
    def calc_consumption(self):
        if self.clothes_type == "coat":
            return self.clothes_param / 6.5 + 0.5
        if self.clothes_type == "suit":
            return 2 * self.clothes_param + 0.3
        return 0


CLOTHES_L10N = {"coat": "пальто", "suit": "костюм"}
fabric_clothes = [Clothes("coat", 50), Clothes("suit", 1.85),
                  Clothes("suit", 1.65), Clothes("coat", 46)]
accu = 0
for clothes in fabric_clothes:
    accu += clothes.calc_consumption
    print(f"Расход ткани на {CLOTHES_L10N[clothes.clothes_type]}: {clothes.calc_consumption:.2f}")
print(f"Общий расход ткани: {accu:.2f}")

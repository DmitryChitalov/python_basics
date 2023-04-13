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
from enum import Enum
from abc import ABC, abstractmethod


class ClothType(Enum):

    COAT = 0
    COSTUME = 1


class ACloth(ABC):

    __name: str
    __type: 'ClothType'

    def __init__(self, name: str, cloth_type: 'ClothType') -> None:
        self.__name = name
        self.__type = cloth_type

    @abstractmethod
    def calc_cloth(self) -> float:



class Coat(ACloth):
    __size: float

    def __init__(self, name: str, size: float) -> None:
        super().__init__(name, ClothType.COAT)
        self.__size = size

    def calc_cloth(self) -> float:
        return self.__size / 6.5 + 0.5


class Costume(ACloth):
    __height: float

    def __init__(self, name: str, height) -> None:
        super().__init__(name, ClothType.COSTUME)
        self.__height = height

    def calc_cloth(self) -> float:
        return 2 * self.__height + 0.3

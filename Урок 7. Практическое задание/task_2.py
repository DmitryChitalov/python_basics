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

class Clothes(ABC):
    @abstractmethod
    def textile_wastage(self):
        pass

class NeoCoat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def textile_wastage(self):
        coat_result = round(self.size / 6.5 + 0.5, 1)
        return coat_result
        
class AgentSuit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def textile_wastage(self):
        suit_result = round(2 * self.height + 0.3, 1)
        return suit_result

mr_anderson = NeoCoat(51)
agent_smith = AgentSuit(56)
total_textile_wastage = mr_anderson.textile_wastage + agent_smith.textile_wastage

print(f'Расход ткани на пальто: {mr_anderson.textile_wastage}')
print(f'Расход ткани на костюм: {agent_smith.textile_wastage}')
print(f'Общий расход ткани: {total_textile_wastage}')

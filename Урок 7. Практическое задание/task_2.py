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

# print(f"Материал для одежды {((self.cloth_coat / 6.5) + 0.5) / 2}")
# print(f"Материал для одежды {((self.cloth_costume * 2) + 0.3)}")
"""


from abc import ABC, abstractmethod


class AbstClassClothes(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def operation_coat(self, hieght, wieght):
        """
        Метод расчета ткани для пальто
        hieght - высота изделия
        wieght - длина изделия
        """

    @abstractmethod
    def operation_costume(self, hieght, wieght):
        """
        Метод расчета ткани для костюма
        hieght - высота изделия
        wieght - длина изделия
        """


class Clothes(AbstClassClothes):
    """
    Класс проекта расчета суммарного
    расхода ткани на производство одежды
    """

    cloth: str

    coat_total: float
    costume_total: float
    total = 0

    def __str__(self):
        """Что-нибудь выводим"""

        return f'Приступаем к пошиву одежды, типа: {self.cloth}'

    def operation_coat(self, hieght, wieght):
        self.coat_total = (2 * (hieght + wieght) + 0.5) / 100
        Clothes.total += self.coat_total
        return self.coat_total

    def operation_costume(self, hieght, wieght):
        self.costume_total = (2 * (hieght + wieght) + 0.3) / 100
        Clothes.total += self.costume_total
        return self.costume_total

    def over_total(self):
        """Метод подсчета всего материала"""
        return str(f"Всего затрачено материала: {round(Clothes.total, 2)} метров")


coat = Clothes()
coat.cloth = 'Пальто'
print(coat)
coat.operation_coat(hieght=120, wieght=48)

costume = Clothes()
costume.cloth = "Костюм"
print(costume)
costume.operation_costume(168, 48)

total = Clothes()

print(total.over_total())

__author__ = 'AndreiM'
__version__ = "1.0 25.04.2023"
print("\n task_2 \n -------- \n")


from abc import ABC, abstractmethod

class MyAbstractClass(ABC):   #constructor
    @abstractmethod
    def consum(self):
        pass

class Clothes(MyAbstractClass):
    def __init__(self, par='MyAbstractClass'):
        self.par = par
        print('------- class Clothes  ', par)

    @property
    def consum_Coat(self, par):
        pass

    @property
    def consum_Suite(self, par):
        pass

    @property
    def consum(self):
        print('------- consum')
        return round(self.consum_Coat + self.consum_Suite, 2)

class Coat(Clothes):
    @property
    def consum(self):
        res = round(self.par / 6.5 + 0.5, 2)
        Clothes.consum_Coat = res
        return f'Расход ткани на пальто - {self.par}, размером - {res}'

class Suite(Clothes):
    @property
    def consum(self):
        res = round(self.par * 2 + 0.3, 2)   #костюм без подкладки, обычный - *2. С покладкой - *4.9
        Clothes.consum_Suite = res
        return f'Расход ткани на костюм - {self.par}, размером - {res}'

#на пальто - 1,5м ширина ткани (рулон). 4м длина ткани на рост - высокий. Размер 56. XXL.
#на костюм - 1.брюки 1,5м ширина ткани (рулон). 1,9м длина ткани и 2.Жакет 0,9м ширина и 4,2м длина ткани (без прокладки) на рост - высокий
#предусматриваем на костюм, всего - 1,5м ширина рулона и 4м длина (1,9 + 2,1). Размер 56. XXL.

o = Clothes()
c = Coat(56) #размер - рост до 180см, охват талии/груди - до 120. Размер 56 (XXL)
print(c.consum)
s = Suite(3) #размер - рост до 180см, охват талии/груди - до 120 (XXL) = 1.8+1.2 = 3
print(s.consum)
print(f'Общий расход ткани = {o.consum}')



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
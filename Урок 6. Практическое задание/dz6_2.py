#  Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Постройка дороги')

    def need(self):
        self.weigth = 25
        self.tickness = 0.05
        ndd = self.length * self.width * self.weigth * self.tickness
        print(f'Надо {ndd} тонн для постойки дороги')


road_to_village = Road(2000, 5)
road_to_village.need()

#Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

wight_sm = int(input("вес одного кв метра дороги (кг) ->"))
sm_road = int(input("толщина дороги (см)->"))
sm_road_res = sm_road/1000

class Road:
    _length = int(input("Введите длину дороги (м)->"))
    _windth = int(input("введите ширину дороги (м)->"))

    @staticmethod
    def formula(self, wight_sm, sm_road):
        wight_road = self._length*self._windth*wight_sm*sm_road_res
        print(f'масса дороги (т) -> {wight_road}')

my_road = Road()
my_road.formula(my_road, wight_sm, sm_road_res)

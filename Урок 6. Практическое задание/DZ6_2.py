class Road:
    m_1_road = 25
    thickness_road = 0.05

    def __init__(self, length, width):
        self._lenght = float(length)
        self._widht = float(width)

    def asphalt_mass(self):
        mass = (self._lenght * self._widht * Road.m_1_road * Road.thickness_road) / 1000
        print(f'Для укладки указанной дороги понадобится {mass} т асфальта')

my_road = Road(20, 5000)
my_road.asphalt_mass()

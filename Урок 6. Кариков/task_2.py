
class Road:
    weight = 25
    height = 0.05

    def __init__(self, width, length):
        self._width = width
        self._length = length


    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * Road.weight * Road.height / 1000
        print(f'Необходимо {round(asphalt_mass)} тонн асфальта')


r = Road(20, 5000)
r.asphalt_mass()
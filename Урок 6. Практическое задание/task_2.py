class Road:
    mass = 25
    thickness = 0.1

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def raschet(self):
        rez = self.mass * self.thickness * self._length * self._width / 1000
        print(f"Итоговая масса - {rez} тонн")


a = Road(200, 50)
a.raschet()

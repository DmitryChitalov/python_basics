class Road:

    def __init__(self, length, width, weight_asphalt, thickness):
        self._length = length
        self._width = width
        self.weight_asphalt = weight_asphalt
        self.thickness = thickness

    def total_weight(self):
        return self._length * self._width * self.weight_asphalt * self.thickness


a = Road(20, 5000, 25, 0.05)
print(a.total_weight())

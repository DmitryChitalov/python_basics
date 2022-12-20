class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_count(self, mass_meter, depth):
        self.mass_meter = mass_meter
        self.depth = depth
        print(self._length * self._width * mass_meter * depth)

r = Road(50, 5)
r.mass_count(15, 5)
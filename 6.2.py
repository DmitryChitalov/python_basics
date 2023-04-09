class Road:
    __mass: float = 25.0
    _length: float
    _width: float

    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def calculate(self, depth: float = 1):
        return (self._length * self._width * self.__mass * depth) / 1000


road = Road(20, 5000)
calculation = road.calculate(5)

print(f"{calculation} т")
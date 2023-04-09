class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_weight(self, thickness, weight_per_sq_meter):
        return self._length * self._width * thickness * weight_per_sq_meter / 1000

my_road = Road(20, 5000)
asphalt_weight = my_road.asphalt_weight(thickness=5, weight_per_sq_meter=25)
print(f"Масса асфальта для покрытия всей дороги: {asphalt_weight} т.")
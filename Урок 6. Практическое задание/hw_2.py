class Road:
    weidht = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._lenght = length
        self._widht = width

    def calc(self):
        res = (self._lenght * self._widht * Road.weidht * Road.thickness) / 1000
        print(f'Потребуется {res} тонн')

r_obj = Road(20, 5000)
r_obj.calc()
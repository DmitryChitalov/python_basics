class Road:
    def calculation(self, depth, weight, lenght, width):
        self._lenght = lenght
        self._width = width
        print(f"Результат расчета: %.f т." % float(self._lenght * self._width * depth * weight / 1000))

a = Road()
a.calculation(int(input("Толщина: ")), int(input("Вес: ")), int(input("Длина: ")), int(input("Ширина: ")))

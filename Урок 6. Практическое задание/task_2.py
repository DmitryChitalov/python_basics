class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def square(self):
        return self._length * self._width



class MassAsphalt(Road):
    pass


i_vars = MassAsphalt(20, 5000).square()
print(i_vars)
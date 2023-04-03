# ����������� ����������� ��� ����� ���� �������

class NonNegative:
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('�� ����� ���� ������������� ������!')
        instance.__dict__[self.my_attr] = value


class Road:
    weight = 25
    thickness = 0.05
    _length = NonNegative()
    _width = NonNegative()

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width

    def intake(self):
        intake = self._length * self._width * self.weight * self.thickness
        print(
            f' ����� �������� �����������  ��� �������� ����� ������� -'
            f' {intake} �� =  {intake / 1000} �.')


all_road = Road(20, 5000)
all_road.intake()

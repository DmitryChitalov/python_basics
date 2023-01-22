from abc import abstractmethod


class clothes:
    def __init__(self, V, H):
        self.V = V
        self.H = H

    @abstractmethod
    def get_square(self):
        pass

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани = {round((self.V / 6.5 + 0.5) + (self.H * 2 + 0.3))}')


class coat(clothes):
    def __init__(self, V, H):
        super().__init__(V, H)

    def get_sqaure(self):
        self.square = self.V / 6.5 + 0.5
        return (f'Ткань на пальто {self.square}')

    def __str__(self):
        return f'Пальто считается по V= {self.V}'


class jacket(clothes):
    def __init__(self, V, H):
        super().__init__(V, H)

    def get_square(self):
        self.square = round(self.H * 2 + 0.3)
        return (f'Ткань на костюм =  {self.square}')

    def __str__(self):
        return f'Костюм считаем по H =  {self.H}'


coat = coat(2, 4)
jacket = jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(jacket.get_square())
print(coat.get_square())

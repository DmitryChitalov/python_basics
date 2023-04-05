class Aaa:
    def __init__(self, c, d):
        self.c = int(c)
        self.d = int(d)

    def e(self):
        if self.d > 0:
            return self.c / self.d
        else:
            return f"Все еще {self.c} ))))"


b = Aaa(input(f"Введите делимое"), input(f"Введите делитель"))
print(b.e())
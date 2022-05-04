class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Start rendering.")
class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return "Uses Pen"
class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return "Uses Pencil"
class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return "Uses Handle"
pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
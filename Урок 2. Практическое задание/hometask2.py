# реализовать метакласс. позволяющий создавать всегда один и тот же объект класса

class Meta(type):
    example = None

    def __call__(self):
        if self.example is None:
            self.example = super().__call__()
        return self.example

class MyClass(metaclass = Meta):
    pass

o_1 = MyClass()
o_2 = MyClass()
o_3 = MyClass()
o_4 = MyClass()
print(o_1 is o_4)
print(o_2 is o_3)
print(o_3 is o_4)
print(o_2 is o_3)
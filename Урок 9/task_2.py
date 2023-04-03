'''
–еализовать метакласс. позвол€ющий создавать всегда один и тот же объект класса
'''


class TestMeta(type):
    example = None

    def __call__(self):
        if self.example is None:
            self.example = super().__call__()
        return self.example


class MyClass(metaclass=TestMeta):
    pass


ob_1 = MyClass()
ob_2 = MyClass()
ob_3 = MyClass()
ob_4 = MyClass()

print(ob_1 is ob_4)
print(ob_2 is ob_3)
print(ob_3 is ob_4)
print(ob_2 is ob_3)

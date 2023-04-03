# –еализовать метакласс. позвол€ющий создавать всегда один и
# тот же объект класса

class DocMeta(type):
    def __int__(self, *args, **kwargs):
        self.__instance = []

    def __call__(self, *args, **kwds):
        if self.__instance is None:
            self.__instance = super().__call__()
            return self.__instance


class MyClass(metaclass=DocMeta):
    pass


ob_1 = MyClass()
ob_2 = MyClass()

print(ob_1 is ob_2)

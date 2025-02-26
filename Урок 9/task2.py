class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value


# Пример использования
obj1 = MyClass(1)
obj2 = MyClass(2)

print(obj1 is obj2)  # True, потому что obj1 и obj2 являются одним и тем же объектом
print(obj1.value)  # 1
print(obj2.value)  # 1, так как obj1 и obj2 ссылаются на один и тот же объект

obj1.value = 3
print(obj2.value)  # 3, потому что значение было изменено у одного и того же

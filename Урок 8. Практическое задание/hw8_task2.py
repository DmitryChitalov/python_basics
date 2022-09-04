class OwnException(Exception):
    def __init__(self, param):
        self.param = param


def division():
    try:
        a = int(input("Введите делимое: "))
        b = int(input("Введите делитель: "))
        if b == 0:
            raise OwnException("На ноль делить нельзя")
        else:
            print(f"Результат: {a / b}")
    except OwnException as err:
        print(err)


print(division())

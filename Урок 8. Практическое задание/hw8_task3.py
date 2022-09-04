class OwnException(Exception):
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return self.param


inp_list = input(f"Введите числа через запятую: ")
new_list = inp_list.split(",")
print(f"Вы ввели следующий список: {new_list}")


def exc_int():
    try:
        for el in new_list:
            if not el.isnumeric():
                raise OwnException("В этом списке есть нечисловые элементы")
    except OwnException as err:
        print(err)


print(exc_int())

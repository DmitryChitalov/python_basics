class OnlyNumbersError(Exception):
    pass


class OnlyNumbersList(list):
    def append(self, item):
        if not isinstance(item, (int, float)):
            raise OnlyNumbersError("Список может содержать только цифры!")
        super().append(item)


my_list = OnlyNumbersList()

while True:
    try:
        num = input("Введите число: ")
        if not num:
            break
        my_list.append(float(num))
    except OnlyNumbersError as e:
        print("Ошибка: ", e)

print("Список чисел: ", my_list)

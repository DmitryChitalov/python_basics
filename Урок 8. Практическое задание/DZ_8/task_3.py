# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список
# необходимо только числами. Класс-исключение должен контролировать типы данных элементов списка.

class NotIntError(Exception):
    def __init__(self, text):
        self.text = text

my_list = []
while True:
    try:
        val = input('Введите значения и нажимайте Enter или stop (для прекращения ввода) - ')
        if val == "stop":
            break
        if not val.isdigit():
            raise NotIntError("введен не корректный символ")
    except NotIntError as err:
        print(err)
    else:
        my_list.append(val)
print(my_list)
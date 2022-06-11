"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        inp_a = input("Введите значения: ")
        if inp_a == "q":
            break
        if inp_a.isnumeric() == True:
            my_list.append(inp_a)
        else:
            raise OwnError("Введено не число")
        print(my_list)
    except OwnError as err:
        print(err)
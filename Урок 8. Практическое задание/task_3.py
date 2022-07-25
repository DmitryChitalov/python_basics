"""
Задание 3.
Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class CheckNumber(Exception):
    def __init__(self, error):
        self.error = error


num_lst = []
while True:
    try:
        x_element = input("Введите число, q - выход: ")
        if x_element.isdigit():
            num_lst.append(int(x_element))
        elif x_element == "q":
            print("Завершение программы")
            break
        else:
            print("Это не число")
    except CheckNumber as err:
        print(err)
print(num_lst)

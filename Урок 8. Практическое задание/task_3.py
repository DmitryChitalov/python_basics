"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class MyClass(Exception):
    def __init__(self, text):
        self.text = text
        super().__init__(self.text)
def x_list():
    y_list = []
    while True:
        try:
            my_val = input("Введите число: ")
            if my_val == "end":
                break
            if not my_val.isdigit():
                raise MyClass
            y_list.append(int(my_val))
        except MyClass as my_error:
            print(my_error)
    return y_list
print(x_list())




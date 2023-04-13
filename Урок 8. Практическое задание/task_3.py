"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class NumbersList(Exception):
    def __init__(self, txt):
        self.txt = txt


user_list = []

for i in range(10):
    try:
        value = input("Enter integers or stop to exit the process:")
        if value == "stop":
            break
        if not value.isdigit():
            raise NumbersList(value)
        user_list.append(int(value))
    except NumbersList as err:
        print("Not a number ", err)

print(user_list)


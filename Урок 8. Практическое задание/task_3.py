"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class MyError(Exception):
    def __init__(self, parm_1):
        self.message = parm_1


user_list = input("Введите числа через пробел: ")
number_list = user_list.split()
number=0
for i in number_list:
    number = number + 1
    try:
        if not i.isnumeric():
            raise MyError(f"{number}-ый элемент списка иммет неверный фoрмат")
    except MyError as err:
        print(err)
    else:
        print(f"{number}-ый элемент списка иммет верный фoрмат")
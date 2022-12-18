"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class MyError(Exception):
    def __init__(self, arg_1):
        self.msg = arg_1


user_list = input("Введите числа через пробел: ")
numb_list = user_list.split()
num_list = []
for i in numb_list:
    try:
        i = float(i)
        num_list.append(i)
    except:
        num_list.append(i)

num=0
for i in num_list:
    num = num + 1
    try:
        if i == str(i):
            raise MyError(f"Ошибка! {num}-й элемент списка не число")
    except MyError as err:
        print(err)
    else:
        print(f"Верно. {num}-й элемент списка есть число")

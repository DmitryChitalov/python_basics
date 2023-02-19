"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
a = ""
while True:
    try:
        a = input("Введите число: ")
        if a == "stop":
            break
        elif a.isdigit():
            my_list.append(a)
        else:
            raise MyException("Вводите только целые числа!")
    except MyException as e:
        print(e.txt)

print(my_list)

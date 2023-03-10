"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class num_exeption(Exception):
    def __init__(self, txt):
        self.txt = txt

new_list = []
x = ""
while True:
    try:
        x = input("Введите число: ")
        if x == "**":
            break
        elif x.isdigit():
            new_list.append(x)
        else:
            raise num_exeption("Вводите только целые числа!")
    except num_exeption as z:
        print(z.txt)

print(new_list)
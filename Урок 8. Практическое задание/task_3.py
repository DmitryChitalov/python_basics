"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


class MyControlInput(Exception):
    def __init__(self, txt):
        self.txt = txt


int_list = []
while True:
    try:
        inp_data = input("Введите число для добавления в список, для выхода введите exit: ")

        if inp_data == "exit":
            break

        if not is_integer(inp_data):
            raise MyControlInput(inp_data)
        int_list.append(int(inp_data))
    except MyControlInput as err:
        print("Введите целое число")

print(f"Результат: {int_list}")

"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

def is_integer(v):
    try:
        float(v)
    except ValueError:
        return False
    else:
        return float(v).is_integer()


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


int_lst = []
while True:
    try:
        inp_data = input("Ввести число для списка, для выхода - !: ")

        if inp_data == "!":
            break

        if not is_integer(inp_data):
            raise MyException(inp_data)
        int_lst.append(int(inp_data))
    except MyException as err:
        print("Введено не число, повторить попытку")

print(f"В результате: {int_lst}")

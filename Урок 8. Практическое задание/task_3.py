"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class MyError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


def num_list():
    if __name__ == '__main__':
        my_list = []

        while True:
            val = input("Введите число, или 'q' для выхода: ")

            if val == "q":
                break

            try:
                if not val.isdecimal():
                    raise MyError(f"'{val}' вы ввели не число!")

                my_list.append(int(val))
            except MyError as err:
                print(err)

        print(my_list)


num_list()

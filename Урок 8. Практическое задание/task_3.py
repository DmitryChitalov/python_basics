"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


def filling_list():
    if __name__ == '__main__':
        my_list = []

        while True:
            user_input = input("Введите число для заполнения списка, или 'q' для выхода: ")

            if user_input == "q":
                break

            try:
                if not user_input.isdecimal():
                    raise NotNumberError(f"'{user_input}' вы ввели не число!")

                my_list.append(int(user_input))
            except NotNumberError as err:
                print(err)

        print(my_list)


filling_list()

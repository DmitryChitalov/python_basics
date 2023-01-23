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


if __name__ == '__main__':
    my_list = []

    while True:
        user_input = input("Введите число для списка, или 'stop' для выхода: ")

        if user_input == "stop":
            break

        try:
            if not user_input.isdigit():
                raise NotNumberError(f"'{user_input}' has not numerical format")

            my_list.append(int(user_input))
        except NotNumberError as e:
            print(e)

    print(my_list)


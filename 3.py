"""
Задание 3.
Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class NotNumError(Exception):
    def __init__(self, error_message="Только числа!"):
        self.error_message = error_message
        super().__init__(self.error_message)


if __name__ == '__main__':
    new_list = []

    while True:
        try:
            inpt = input("Введите число (q для выхода): ")
            if inpt == "q":
                break
            if not inpt.isnumeric():
                raise NotNumError('Упс')
            new_list.append(int(inpt))
        except NotNumError as err:
            print(err)

    print("Result:", new_list)

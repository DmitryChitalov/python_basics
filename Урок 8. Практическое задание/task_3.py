"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NonNumericListError(Exception):
    def __init__(self, message="Список должен содержать только числа"):
        self.message = message
        super().__init__(self.message)


my_list = []

while True:
    try:
        user_input = input("Введите число для списка (или 'q' для выхода): ")
        if user_input == "q":
            break
        if not user_input.isnumeric():
            raise NonNumericListError
        my_list.append(int(user_input))
    except NonNumericListError as e:
        print(e)

print("Список чисел:", my_list)

"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class NumError(Exception):
    def __init__(self, error_message="Only numbers!"):
        self.error_message = error_message
        super().__init__(self.error_message)


new_list = []

while True:
    try:
        test_input = input("Enter a number (or 'x' to exit): ")
        if test_input == "x":
            break
        if not test_input.isnumeric():
            raise NumError
        new_list.append(int(test_input))
    except NumError as k:
        print(k)

print("Result:", new_list)
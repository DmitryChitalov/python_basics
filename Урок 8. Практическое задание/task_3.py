"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NotOnlyNumbersException(Exception):
    def __init__(self, current_list, value):
        self.current_list = current_list
        self.value = value

    def __str__(self):
        return f'The inputted number \'{self.value}\' cannot be added to only numbers list: {self.current_list}'


class ErrorController:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        while True:
            inputted_value = ''
            try:
                inputted_value = input('Enter the number: ')
                self.my_list.append(int(inputted_value))
                print(f'Current list: {self.my_list}')
            except:
                # raise NotOnlyNumbersException(self.my_list, inputted_value)
                if inputted_value == 'stop':
                    return
                print(f"Invalid value")


error = ErrorController()
error.my_input()

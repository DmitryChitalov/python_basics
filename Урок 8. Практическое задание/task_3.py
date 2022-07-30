"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class CheckExept(Exception):
    def __init__(self, testenter):
        self.testenter = testenter


def check_type(my_enter):
    if my_enter.isdigit():
        return my_enter
    else:
        try:
            float(my_enter)
            return my_enter
        except ValueError:
            raise CheckExept('Вы ввели не число, требуется вводить только числа.')


input_request = ''
total_list = []
print("Введите число и нажмите Enter. Для выхода - 'exit'")
while input_request != 'exit':
    try:
        input_request = input(">>> ")
        total_list.append(check_type(input_request))
    except CheckExept as exit:
        if input_request != 'exit':
            print(exit.testenter)
print(f"Cписок - {total_list}")
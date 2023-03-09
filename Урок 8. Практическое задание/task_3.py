"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class MyNotNumberError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
 
my_list = []

while True:
    try:
        value = input('Введите число в список: ')
        if value == 'exit':
            break
        elif not value.isdigit():
            raise MyNotNumberError('Вы ввели не число!', value)
        else:
            my_list.append(int(value))
    except MyNotNumberError as e:
        print(e)
print(my_list)
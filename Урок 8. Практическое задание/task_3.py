"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NaNError(Exception):
    def __init__(self, text):
        self.text = text


def number_filter(string):
    if string.isdigit():
        return string
    else:
        try:
            float(string)
            return string
        except ValueError:
            raise NaNError(f"Ошибка: '{string}' - введенные данные не являются числом!!!")


input_text = ''
counter = 1
numbers_list = []
print("Введите числа по одному, для выхода введите 'stop'")
while input_text != 'stop':
    try:
        input_text = input(f"{counter}: ")
        numbers_list.append(number_filter(input_text))
        counter += 1
    except NaNError as e:
        if input_text != "stop":
            print(e.text)

print(f"По итогу вы ввели:\n{numbers_list}")

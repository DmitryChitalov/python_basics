"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class NumberError(Exception):
    def __init__(self, txt):
        self.txt = txt
def numberfilter(string):
    if string.isdigit():
        return string
    else:
        try:
            float(string)
            return string
        except ValueError:
            raise NumberError(f'Ошибка: {string} - введено не число')
input_txt = ''
counter = 1
numbers_list = []
print("Вводите числа по одному. Для выхода введите 'стоп'")
while input_txt != 'стоп':
    try:
        input_txt = input(f"{counter}: ")
        numbers_list.append(numberfilter(input_txt))
        counter += 1
    except NumberError as e:
        if input_txt != 'stop':
            print(e.txt)
print(f"Result list:\n{numbers_list}")

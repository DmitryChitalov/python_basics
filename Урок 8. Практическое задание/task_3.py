"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class ChekType(Exception):
    def __init__(self, list):
        self.list = list

    @staticmethod
    def number_filter(string):
        if string.isdigit():
            return string
        else:
            try:
                float(string)
                return string
            except ValueError:
                raise ChekType(f"Вводите только числа!")

input_txt = ''
counter = 1
numbers_list = []
print("Введите числа по одному, для выхода введите 'q'")
while input_txt != 'q':
    try:
        input_txt = input(f"{counter}: ")
        numbers_list.append(ChekType.number_filter(input_txt))
        counter += 1
    except ChekType as e:
        if input_txt != 'q':
            print(e.list)

print(f"Полученный список чисел:\n{numbers_list}")
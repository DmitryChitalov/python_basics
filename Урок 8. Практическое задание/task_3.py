"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class MyException(ValueError):
    '''Собственный класс исключения'''
    def __init__(self, txt):
        self.txt = txt


list_nums = []

while True:
    user_ent = input('Введите число: ')
    if user_ent.lower() == 'стоп':
        break

    try:
        if user_ent.isdigit():
            list_nums.append(int(user_ent))
        else:
            raise MyException("Вы вводите не число! Нужно ввести только число!")
    except MyException as err:
        print(err)
    else:
        print(f"Все хорошо. У нас уже следующий набо чисел: {list_nums}")

print(f"Мы закончили. Вот результат: {list_nums}")

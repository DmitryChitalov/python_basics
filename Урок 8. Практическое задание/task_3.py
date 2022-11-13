"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class MyListError(Exception):
    def __init__(self):
        print("Exception: неверный элемент списка!")

    @staticmethod
    def test_element(arg):
        """
        Проверяет аргумент-строку на содержание в ней только чисел
        :param arg: строка для проверки
        :return: True - если в строке только числа, False - в остальных случаях
        """
        return arg.isdigit()


lst = []

while True:
    s = input("Введите число для списка (пустая строка для завершения:")
    if s == '':
        break
    try:
        if not MyListError.test_element(s):
            raise MyListError
    except MyListError:
        print("Сработало исключение. Введите число!")
    else:
        lst.append(int(s))

print(f"Введены элементы в список: {lst}")

"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class IsNotInteger(Exception):
    def __init__(self, msg):
        self.msg = msg


input_integer = 0
array_integers = []
while input_integer != 999:
    print("Для завершения программы введите \"999\"")
    try:
        input_integer = int(input("Введите число: "))
        if type(input_integer) != int:
            raise IsNotInteger("Что ты творишь?!")
        else:
            if input_integer != 999:
                array_integers.append(input_integer)
    except ValueError:
        print("Эти каракули - не число!")
print(array_integers)

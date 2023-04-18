"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class OwnError(Exception):
    pass


inp_data = input("Введите числа через пробел: ")
inp_data_split = inp_data.split(" ")
counter = 0
while counter < len(inp_data_split):
    try:
        if not inp_data_split[counter].lstrip("-").isnumeric():
            raise OwnError(f"{inp_data_split[counter]} - Не число")
    except OwnError as err:
        inp_data_split.pop(counter)
        counter -= 1
        print(err)
    counter += 1
print(f"Итоговый результат: {inp_data_split}")


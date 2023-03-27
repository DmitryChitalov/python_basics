"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class IsNotNumberTypeException(Exception):
    def __init__(self, txt):
        self.txt = txt


input_data = input('Вам необходимо ввести через пробел набор данных: ').split()
num_data = []
for el in input_data:
    try:
        if el.isdigit():
            num_data.append(int(el))
        else:
            raise IsNotNumberTypeException(f"{el} - не числовые данные")
    except IsNotNumberTypeException as e:
        print(e.txt)
print(num_data)

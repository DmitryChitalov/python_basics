"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class NotNumbersInListError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def is_number_list(lst):
    for item in lst:
        if not isinstance(item, (int, float)):
            raise NotNumbersInListError("Список должен содержать только числа!")

lst = []
while True:
    try:
        item = input("Введите число или 'stop' для завершения: ")
        if item == "stop":
            break
        item = float(item)
        lst.append(item)
    except ValueError:
        print("Ошибка: введите число")
    except NotNumbersInListError as e:
        print(f"Ошибка: {e.message}")

is_number_list(lst)
print(f"Список чисел: {lst}")

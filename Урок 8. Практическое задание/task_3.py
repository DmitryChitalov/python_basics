"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class NonNumericListError(Exception):
    pass

def create_numeric_list():
    num_list = []
    while True:
        try:
            num = input("Enter a number (or 'stop' to finish): ")
            if num == "stop":
                break
            elif not num.isdigit():
                raise NonNumericListError("List must contain only numbers")
            num_list.append(int(num))
        except NonNumericListError as e:
            print(e)
    return num_list

try:
    numeric_list = create_numeric_list()
    print(f"Numeric list: {numeric_list}")
except ValueError:
    print("Invalid input")
except NonNumericListError as e:
    print(e)

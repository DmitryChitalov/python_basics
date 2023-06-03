"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class NotNumberError(Exception):
    pass

def get_numbers():
    numbers = []
    while True:
        try:
            user_input = input("Введите число или 'stop' для завершения: ")
            if user_input == 'stop':
                break
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Ошибка: допустимо вводить только числа")
        except NotNumberError as e:
            print(f"Ошибка: {e}")
    return numbers

class NumberList(list):
    def append(self, value):
        if not isinstance(value, (int, float)):
            raise NotNumberError("Допустимо вводить только числа")
        super().append(value)

try:
    number_list = NumberList()
    number_list.extend(get_numbers())
    print(f"Список чисел: {number_list}")
except NotNumberError as e:
    print(f"Ошибка: {e}")
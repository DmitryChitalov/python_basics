"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class ValidateLstError(Exception):
    @staticmethod
    def validate_lst(param_lst):
        for i in param_lst:
            try:
                val = float(i)
            except:
                raise ValidateLstError
                break

    def __str__(self):
        return "В списке есть не числовое значение"


lst = [1, 2, 2]
print(lst)
try:
    ValidateLstError.validate_lst(lst)
except ValidateLstError as error:
    print(error)

lst = [1, "sfds", 2]
print(lst)
try:
    ValidateLstError.validate_lst(lst)
except ValidateLstError as error:
    print(error)

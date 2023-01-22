"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class OwnError(Exception):

    def func_str(self, my_list):
        try:
            for el in my_list:
                if type(el) == str:
                    raise OwnError("в списке присутствует элемент типа данных <<str>>: ")

        except OwnError as err:
            print(err, el)

    def func_bool(self, my_list):
        try:
            for el in my_list:
                if type(el) == bool:
                    raise OwnError("в списке присутствует элемент типа данных <<bool>>: ")
        except OwnError as err:
            print(err, el)


input_list = [2, 1.2, 'str-элемент', bool(20)]
print("Введенный список: ", input_list, "\n")
my_err = OwnError()
my_err.func_str(input_list)
my_err.func_bool(input_list)

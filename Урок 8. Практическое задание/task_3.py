"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NotANumberError(Exception):
    """
    кастомное исключение NaN
    """
    def __init__(self, message) -> None:
        self.__message = message

    @property
    def message(self):
        """
        сообщение исключения
        """
        return self.__message


class ListValidator:
    """
    класс валидатор готового списка
    """
    @staticmethod
    def validate(lst):
        """
        Валидирует список на начие в нем не чисел
        гененрирует NotANumberError если элемент списка не число
        """
        if not isinstance(lst, list):
            raise TypeError("Аргумент должен быть списком")
        index = 0
        for el in lst:
            if not isinstance(el, (int, float)):
                raise NotANumberError(f"Элемент со значение '{el}' в позиции {index} для списка {lst} не является числом!")
            index += 1


test_list1 = [5, 8, -4, "17", "ab", 9]
try:
    ListValidator.validate(test_list1)
except NotANumberError as err:
    print(err.message)

test_list2 = [5, 8, -4, 9]
try:
    ListValidator.validate(test_list2)
except NotANumberError as err:
    print(err.message)
else:
    print(f"{test_list2} is a list of numbers")

print()

result = []
print("Введите число или Enter для завершения")
while True:
    user_data = input("> ").strip()
    if user_data == "":
        break

    try:
        try:
            val = float(user_data)
        except ValueError as ve:
            raise NotANumberError(f"значение {user_data} не является числом!") from ve
        result.append(val)
    except NotANumberError as nan:
        print(nan.message)

print(f"Полученный список:\n{result}")

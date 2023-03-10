"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class NotDigitException(Exception):
    pass


num_list = []
is_cancel = False
is_digit = True
while is_cancel == False:
    try:
        ch = input('Введите число: ')
        if (ch == ''):
            is_cancel = True
            continue
        try:
            digit = int(ch)
        except ValueError:
            is_digit = False
        if is_digit == False:
            raise NotDigitException(f'{ch} - не число')
        num_list.append(int(ch))
    except NotDigitException as ex:
        print(ex)
        is_digit = True

print(num_list)

"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class MyOwnExc(Exception):
    def __init__(self, txt):
        self.txt = txt


num_lst = []
while True:
    try:
        elem = input("Введите число или stop для завершения: ")
        if elem == 'stop':
            break
        elif elem.isdigit():
            num_lst.append(int(elem))
        else:
            raise MyOwnExc("Вы ввели не число")
    except MyOwnExc as e:
        print(e.txt)

print(num_lst)
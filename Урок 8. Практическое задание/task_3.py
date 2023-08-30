"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class MyException(Exception):
    txt = "PROBLEM!!!! Value can't be converted to int"

    def __str__(self):
        return self.txt


final_list = []
while True:
    val = input("Please enter number or 'stop' for finish ")
    if val == 'stop':
        break
    else:
        try:
            if val.isnumeric():
                final_list.append(int(val))
            else:
                raise MyException
        except MyException as err:
            print(err)

print(final_list)
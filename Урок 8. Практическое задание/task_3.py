"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
#Task_3
class MyException(Exception):

    def __str__(self):
        return f"Ошибка! Только целые числа"

control = True
mylist = []
i = 0
while control:
    try:
        while i < 3:
            num = input('Введите три целых числа для списка ')
            if not num.isdigit():
                raise MyException
            mylist.append(int(num))
            print('Список: ', mylist)
            i += 1
        control = False
    except MyException as e:
        print(e)

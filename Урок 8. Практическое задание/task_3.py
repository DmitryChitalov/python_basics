"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

self_res = []
while True:
    try:
        data = input("Ввеcти число или s для завершения: ")
        if data == 's':
            break
        elif data.isdigit():
            self_res.append(int(data))
        else:
            raise MyException("Ввели не число")
    except MyException as er:
        print(er.txt)

print(self_res)

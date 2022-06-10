"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


import traceback


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class CheckAndAdd:

    def __init__(self):
        self.__result = []
        while True:
            data = input('Number: ')
            try:
                self.__result.append(int(data))
            except ValueError as e:
                if data == 'stop':
                    break
                print('Error:\n', traceback.format_exc())
            except Exception as e:
                if data == 'stop':
                    break
                raise MyException('Another error')

    def __str__(self):
        return ', '.join(map(str, self.__result))


if __name__ == '__main__':
    c = CheckAndAdd()
    print(c)
    d = CheckAndAdd()
    print(d)
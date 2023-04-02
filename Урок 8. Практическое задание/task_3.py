"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class Error:
    def __init__(self, *args):
        self.my_list = []

    def mylist(self):
        while True:
            try:
                val = int(input('Введите значения: '))
                self.my_list.append(val)
                print(f'Текущий список: {self.my_list} \n ')
            except:
                print(f"Ввод только чисел  ")
                stop = input(f'Введите -ex для ВЫХОДА или введите ЛЮБОЙ символ для продолжения ')

                if stop == '-ex':
                    return f'Выход'
                else:
                    print(try_except.mylist())

try_except = Error(1)
print(try_except.mylist())

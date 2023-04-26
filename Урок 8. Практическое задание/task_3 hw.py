__author__ = 'AndreiM'
__version__ = "1.0 25.04.2023"
print("\n task_3 \n -------- \n")


class Except_Error:
    def __init__(self, *args):
        self.my_lst = []

    def my_input(self):
        while True:
            try:
                val = float(input('Введите значения одной строкой без пробелов и следом нажмите Enter \n > '))
                self.my_lst.append(val)
                print(f'Текущий список - {self.my_lst} \n ')
            except ValueError:
                print(f'Недопустимое значение - строка и булево')
                y_or_n = input(f' > Повторный ввод? yes (y) / no (n) or quit (q:): ')

                if y_or_n == 'yes' or y_or_n == 'y':
                    print(t.my_input())
                elif y_or_n == 'no' or y_or_n == 'n':
                    return f'Вы вышли...'
                elif y_or_n == 'q:':
                    return f'Вы вышли...'

t= Except_Error(1)
print(t.my_input())

"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
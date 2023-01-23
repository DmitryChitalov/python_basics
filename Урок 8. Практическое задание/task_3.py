"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class Error(Exception):
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = input('Введите значения и нажимайте Enter - ')
                if val == 'stop':
                    print(f'Список сформирован {self.my_list}')
                    break
                val = int(val)
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except ValueError:  # Error(Exception) не отрабатывает по задумке
                print('Это не цифра')


try_except = Error(1)
print(try_except.my_input())

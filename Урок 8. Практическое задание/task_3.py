"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class Check:
    def __init__(self, *args):
        self.new_list = []

    def my_input(self):


        while True:
            try:
                val = int(input('Введите числовые значения,в конце нажмите Enter - '))
                self.new_list.append(val)
                print(f'Сформирован список - {self.new_list} \n ')
            except:
                print(f"Ошибка! Допустимы только числа.")
                y_or_n = input(f'Продолжить? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Завершено'
                else:
                    return f'Завершено'


try_except = Check(1)
print(try_except.my_input())

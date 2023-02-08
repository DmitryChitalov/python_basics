"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class OnlyDigit:
    def __init__(self, *args):
        self.my_list = []

    def input_digit(self):
        while True:
            val = input('Вводите числа с новой строки.\n(press Q to exit)\n>  ')
            try:
                val = int(val)
                self.my_list.append(val)
                print(f'Обновлённый список: {self.my_list} \n')
            except ValueError:
                if val == 'Q' or val == 'q':
                    return f'Exit... Goodbye!'
                else:
                    print(f"Введено значение неправильного типа!\n")


try_except = OnlyDigit(1)
print(try_except.input_digit())

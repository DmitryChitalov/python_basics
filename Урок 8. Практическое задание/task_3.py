"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class Err:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                num = int(input("Введите цифры или символы: "))
                self.my_list.append(num)
                print(f'Введенные значения: - {self.my_list} \n ')
            except:
                print("Недопустимое значение (строка или булево)")
                y_or_n = input('Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return 'Вы вышли'
                else:
                    return 'Вы вышли'


try_except = Err(1)
print(try_except.my_input())
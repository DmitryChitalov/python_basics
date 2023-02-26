"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class only_numbers:
    def __init__(self, *args):
        self.my_list = []

    def my_numbers(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter для выхода: '))
                self.my_list.append(val)
                print(f'Текущий список: {self.my_list} \n ')
            except:
                print(f"Недопустимый тип")
                y_or_n = input(f'Попробовать еще раз? да/нет ')
                if y_or_n == 'да':
                    print(try_except.my_numbers())
                elif y_or_n == 'нет':
                    return f'Сеанс завершен'
                else:
                    return f'Сеанс завершен'


try_except = only_numbers(1)
print(try_except.my_numbers())
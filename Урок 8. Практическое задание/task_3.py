"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class MyError(Exception):
    
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data
    

if __name__ == '__main__':
    my_list = []

    while True:
        my_input = input('Введите число и нажмите Enter, выход - exit: ')
        if my_input == 'exit':
            break

        try: 
            if not my_input.isdigit():
                raise MyError('Неверный формат')
            my_list.append(my_input)
            print(f'Список выглядит так: {my_list}')
        except MyError as e:
            print(e)

    print(my_list)

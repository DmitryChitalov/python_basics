"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class NotIsNumber(Exception):
    def __init__(self, txt):
        self.txt = txt

nums = []
while True:
    user_num = input('Введите данные (только числа): ')
    if user_num == 'off':
        print('Bye')
        break
    try:
        if not user_num.isdigit():
            raise NotIsNumber('\nОшибка ввода, разрешены только числа. Попробуйте еще раз')
    except NotIsNumber as nin:
        print(nin)
    else:
        nums.append(user_num)
    finally:
        print(f'Мы ввели чисел: {len(nums)}')

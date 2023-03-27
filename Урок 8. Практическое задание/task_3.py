"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class MyException(Exception):
    pass

array = []

print('Для выхода введите stop')
while True:
    try:
        number = input('введите число: ')
        if number == 'stop':
            break
        
        if not number.isdigit():
            raise MyException(f'{number} не число, пропускаем')
        array.append(int(number))

    except MyException as ex:
        print(ex)
        
print(array)
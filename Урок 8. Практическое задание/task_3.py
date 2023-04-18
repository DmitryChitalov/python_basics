"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class OnlyNumbErr(Exception):
    pass

def getnumbersonly(string):# принимаем строку , оставляем только цифры
    numbers = []
    for char in string:
        if char.isdigit():
            numbers.append(char)
        elif char != ' ': # иначе пропускаем
            pass
    return ''.join(numbers)


try:
    string = input("Введите строку с цифрами и буквами: ")
    numbersonly = getnumbersonly(string)
    print("Только цифры:", numbersonly)
except OnlyNumbErr as e:
    print("Ошибка:", e)

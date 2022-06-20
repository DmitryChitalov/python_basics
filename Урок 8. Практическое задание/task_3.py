"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class Error:
    def __init__(self, *args):
        self.args = []

    def num(self):
        while True:
            try:
                numbers = int(input('введите число'))
                self.args.append(numbers)
                print(f'Текущий список - {self.args} \n ')
            except:
                print('Ощибка! Вы ввели строку')
                desision = input('Продолжить: y/n?')
                if desision == 'y':
                    print(try_ex.num())
                elif desision == 'n':
                    return ('Выход')
                else: return('Выход')

try_ex = Error(1)
print(try_ex.num())


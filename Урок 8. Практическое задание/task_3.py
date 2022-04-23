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
        self.list = []

    def new_input(self):
        while True:

            try:
                val = int(input('Введите число '))
                self.list.append(val)
                print(f'Текущий список - {self.list} \n ')
            except:
                print("Это не число!")
                decision = input("если хотите закончить, напишите stop, иначе продолжим ")
                if decision == "stop":
                    return "Exit"
                else:
                    print(try_except.new_input())

try_except = Error(1)
print(try_except.new_input())

"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class MyError(ValueError):
    def __init__(self,message='Not numaratic'):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'>>>>>>{self.message}'
my_list = []
my_var= 0
while  my_var !='q':
    my_var = input('введите число, для выхода нажмите q : ')
    try:
        if my_var.isnumeric():
            my_var=int(my_var)
        else :
            if my_var != 'q':
                raise MyError()
    except MyError:
        print(MyError())
    else:
        if my_var != 'q':
            my_list.append(my_var)


print(my_list)
"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class correct_list(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list=input("Введите список чисел через пробел: ").split()
my_num_list=[]
for el_str in my_list:
    try:
        if el_str[0]=='-':
            el=el_str[1:]
        else:
            el=el_str
        if el.isdigit():
            pass
        elif el.count('.')==1:
             for el2 in el.split('.'):
                 if el2.isdigit():
                     pass
                 else:
                     raise correct_list(f"{el_str} не является числом")
        else:
            raise correct_list(f"{el_str} не является числом")
    except correct_list as err:
        print(err)
    else:
        my_num_list.append(el_str)
print(f"Результирующий список чисел: {my_num_list}")

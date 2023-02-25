"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
check_list = [2, 2.5, 2j, 'text']  # список
print("Тип данных: ", type(check_list))  # вывод типа check_list
for i in check_list:  # проверка каждого элемента списка
    print("Тип данных элемента:", f'{i} is {type(i)}')   # вывод типа элемента
# кортеж
check_tuple = (10, 20, 15)
print("Тип данных: ", type(check_tuple))  # вывод типа check_tuple
# множество с изменяемыми данными
check_set = set('hello')
print("Тип данных: ", type(check_set))  # вывод типа check_set
# множество с неизменяемыми данными
check_frozenset = frozenset('hello')
print("Тип данных: ", type(check_frozenset))  # вывод типа check_frozenset
# словарь
check_dict = dict(key_1='el', key_2='le')
print("Тип данных: ", type(check_dict))  # вывод типа check_dict
# булевое значение
check_bool = True
print("Тип данных: ", type(check_bool))  # вывод типа check_bool
# пустое значение
check_NoneType = None
print("Тип данных: ", type(check_NoneType))  # вывод типа check_NoneType

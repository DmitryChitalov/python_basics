"""
Задание 1. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""

int_number = 37
str_word = 'Hi'
float_number = 7.3
bool_type = True
new_list = ['1', 'a']
new_tuple = ('2', 'b')
new_dic = {'number': '3', 'letter': 'b'}
none_type = None
final_list = [int_number, str_word, float_number, bool_type, new_list,
              new_tuple, new_dic, none_type]
for i in final_list:
    print(f'{i} is {type(i)}')

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
var_int = 5
var_float = 5.3
var_bool = False
var_str = "Pip pop"
none_var = None
dict_list = ["var_int", "var_float", "var_bool", "var_str", "dict_list", "none_var", "Sel"]


def type_var(el, var_target):
    print(el, type(var_target), var_target)


for el in dict_list:
    if el == "var_int":
        type_var(el, var_target := var_int)
    elif el == "var_float":
        type_var(el, var_target := var_float)
    elif el == "var_bool":
        type_var(el, var_target := var_bool)
    elif el == "var_str":
        type_var(el, var_target := var_str)
    elif el == "none_var":
        type_var(el, var_target := none_var)
    elif el == "dict_list":
        type_var(el, var_target := dict_list)
    else:
        print("Pupa")

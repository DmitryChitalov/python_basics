"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""

var_int = 5
var_float = 5.3
var_bool = False
var_str = "Pip pop"
dict_list = ["var_int", "var_float", "var_bool", "var_str", "dict_list"]


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
    elif el == "dict_list":
        type_var(el, var_target := dict_list)
    else:
        print("Pupa")


user_name = input("Имя: ")
age = int(input("Возрост: "))
print(f"Привет {user_name}, вам {age} лет")
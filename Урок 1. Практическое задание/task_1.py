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

var_int = 1
var_float = 2.8
var_str = "hello world"
var_bool = True
var_tuple = (1, 2, 3)
var_list = [1, "string", False]
var_dict = {"one": 1, "two": 2}

print(var_int, var_float, var_str, var_bool, var_tuple, var_list, var_dict, sep='\n')

firstname = input("Как вас зовут? ")
age = input("Сколько вам лет? ")
city = input("Из какого вы города? ")

print(f"Ваше имя: {firstname}, Ваш возраст: {age}, Ваш город: {city}")

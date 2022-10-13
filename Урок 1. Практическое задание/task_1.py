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

age = 17
pi_val = 3.1415
str_variant1 = 'Test string 1'
str_variant2 = "Test string 2"
true_val = True
lang_iso1639_1 = ["en", "ru", "tr", "fi"]
tuple_person = (18, "Masha", True, 1.68)
dict_person = {
    "age": 18,
    "name": "Mary",
    "active": True,
    "height": 1.68
}

print("Variables: types and values\n--------------------------------")
print(f"type: {type(age)}, value: {age}")
print(f"type: {type(pi_val)}, value: {pi_val}")
print(f"type: {type(str_variant1)}, value: {str_variant1}")
print(f"type: {type(str_variant2)}, value: {str_variant2}")
print(f"type: {type(true_val)}, value: {true_val}")
print(f"type: {type(lang_iso1639_1)}, value: {lang_iso1639_1}")
print(f"type: {type(tuple_person)}, value: {tuple_person}")
print(f"type: {type(dict_person)}, value: {dict_person}")

print("\nOperations:")
age_soon = 14
age_daughter = 7
age_of_children = age_soon + age_daughter
print(f"Возраст детей {age_soon} + {age_daughter} = {age_of_children}")

print("\nMany references of value:")
ref_one = 123
ref_two = ref_one
print(f"ref_two refers to ref_one: {ref_two}")

user_name = input("\nВедите ваше имя: ")
user_password = input("Ведите ваш пароль: ")
user_age = int(input("Введите ваш возраст: "))

print(f"Ваши данные для входа в аккаунт: имя - {user_name}, пароль - {user_password}, возраст - {user_age}")

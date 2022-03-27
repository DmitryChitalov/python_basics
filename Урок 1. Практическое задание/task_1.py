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

"""ФИО Суслин Александр"""

var1 = var2 = var3 = None
print(var1, var2, var3)

int1 = int(input("Enter integer: "))
float1 = float(input("Enter float: "))
str1 = input("Enter string: ")
print(f"int: {int1}, float: {float1}, string: {str1}")

name = input("Enter your name: ")
password = input("Enter your password: ")
age = int(input("Enter your age: "))
print(f"Credentials: name - {name}, password - {password}, age - {age}")

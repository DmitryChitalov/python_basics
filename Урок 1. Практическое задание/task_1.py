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


age = 31
name = 'Maxim'

print('Hi my name is', name, 'and my age is', age)

user_name = input('What is your name? ')
user_age = int(input('Your age? '))

print(f'Hello, {user_name}! your age is {user_age}.')

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

# Создание и вывод переменных
a = 1
b = 3
print(a, b)

# Запросы у пользователя
name = input('Введите Ваше имя: ')
age = int(input('Введите Ваш возраст: '))
print(f'Ваши данные - {name}, {age} года/ лет')
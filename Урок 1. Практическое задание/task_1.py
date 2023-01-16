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

name = input('Enter your login: ')
password = input('Enter your password: ')

# функция проверки на корректность (в случае, если пользователь введет буквенные значения)
def is_age(userInput):
    while True:
        x = input(userInput)
        try:        
            return int(x)
        except ValueError:
            print('Error. Please enter your age!')

age = is_age('Enter your age: ')

print('\nLogin: ', name)
print('Password: ', password)
print('Your age: ', age)

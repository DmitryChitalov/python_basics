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
usr_name = input('Введите ваше имя \n')
usr_passwd = input('Введите ваш пароль \n')
usr_old = int(input('Введите ваш возраст \n'))
print(f'Ваши данные для входа в аккаунт:\n'
      f'Имя: {usr_name} \n'
      f'Пароль: {usr_passwd} \n'
      f'Возраст: {usr_old} \n')

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
str_var = "Всем привет!"
print(str_var)
int_var = 7325
print(int_var)
float_var = 58.13
print(float_var)
list_var = [1, 'строка', 7, 8]
print(list_var)
dict_var = {1: 'Дата', 2: 'Месяц', 3: 'Год'}
print(dict_var)

dig_1 = int(input('Укажите целое число: '))
dig_2 = int(input('Укажите целое число: '))
dig_3 = int(input('Укажите целое число: '))
print("Вы указали целые числа:", dig_1, dig_2, dig_3)

str_1 = input('Напишите любое слово: ')
str_2 = input('Напишите любое слово: ')
str_3 = input('Напишите любое слово: ')
print("Вы написали слова:", str_1, str_2, str_3)

str_1 = input('Укажите Ваше имя: ')
dig_1 = int(input('Укажите Ваш возраст: '))
str_2 = input('Укажите Ваш пароль для аккаунта: ')
print("Ваши данные для входа в аккаунт:", str_1, dig_1, str_2)

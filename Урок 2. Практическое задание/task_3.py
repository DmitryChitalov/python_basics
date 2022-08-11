"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень', 'Зима']
seasons_dict = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень', 4: 'Зима'}

month_num = int(input('Введите номер месяца: '))

if 0 < month_num < 13:
    season = month_num // 3
    print(f"Результат через список: {seasons_list[season]}")
    print(f"Результат через словарь: {seasons_dict[season]}")
else:
    print('Out of bounds')

"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
month_search = int(input('Введите номер месяца: '))
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
if month_search <= 0 or month_search > 12:
    print('Неверный ввод!')
else:
    print(f'Результат через список: ',end='')
if month_search in [1, 2, 12]:
    print(season_list[0])
elif month_search in [3, 4, 5]:
    print(season_list[1])
elif month_search in [6, 7, 8]:
    print(season_list[2])
elif month_search in [9, 10, 11]:
    print(season_list[3])

season_dict = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
for key_search, value_search in season_dict.items():
    if month_search in value_search:
        print(f'Результат через словарь: {key_search}')

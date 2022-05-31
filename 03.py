month = int(input('Введите номер месяца: '))
if month in [12, 1, 2]:
    print('Зима')
elif month in [3, 4, 5]:
    print('Весна')
elif month in [6, 7, 8]:
    print('Лето')
elif month in [9, 10, 11]:
    print('Осень')

seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)
           }
month = int(input('Введите номер месяца: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)
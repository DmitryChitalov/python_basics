seasons = {'Зима': [12, 1, 2],
           'Весна': [3, 4, 5],
           'Лето': [6, 7, 8],
           'Осень': [9, 10, 11]}

number = int(input('Введите номер месяца: '))

if number in seasons['Зима']:
    print('Это Зима')
if number in seasons['Весна']:
    print('Это Весна')
if number in seasons['Лето']:
    print('Это Лето')
if number in seasons['Осень']:
    print('Это Осень')

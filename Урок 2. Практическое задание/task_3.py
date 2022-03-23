"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

month = int(input('Enter number of month 1 to 12 '))
list_of_seasons = ['winter', 'spring', 'summer', 'autumn']
dic_of_seasons = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
if month == 12 or month == 1 or month == 2:
    print(f'From list {month} is {list_of_seasons[0]}')
    print(f'From dictionary {month} is {dic_of_seasons.get(1)}')
elif month == 3 or month == 4 or month == 5:
    print(f'From list {month} is {list_of_seasons[1]}')
    print(f'From dictionary {month} is {dic_of_seasons.get(2)}')
elif month == 6 or month == 7 or month == 8:
    print(f'From list {month} is {list_of_seasons[2]}')
    print(f'From dictionary {month} is {dic_of_seasons.get(3)}')
elif month == 9 or month == 10 or month == 11:
    print(f'From list {month} is {list_of_seasons[3]}')
    print(f'From dictionary {month} is {dic_of_seasons.get(4)}')
else:
    print('Incorrect month')

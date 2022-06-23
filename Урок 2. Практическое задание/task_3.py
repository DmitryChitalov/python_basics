"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

count = input('Enter month number')
season_dict = {"1": "winter",
               "2": "winter",
               "3": "spring",
               "4": "spring",
               "5": 'spring',
               "6": "summer",
               "7": "summer",
               "8": "summer",
               "9": "autumn",
               "10": "autumn",
               "11": "autumn",
               "12": "winter"}

if (int(count) > 0) and (int(count) < 13):
    print(f'With dict method: {count} month is {season_dict[count]}')
    if count in ["12", "1", "2"]:
        print(f'With list method:{count} month is winter')
    elif count in ["3", "4", "5"]:
        print(f'With list method:{count} month is spring')
    elif count in ["6", "7", "8"]:
        print(f'In list method:{count} month is summer')
    else:
        print(f'With list method:{count} month is autumn')
else:
    print('mistake')
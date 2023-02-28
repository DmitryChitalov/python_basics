"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
# Вариант черзе список
month = int(input('Введите число месяца: '))

month_name = ['Winter','Autumn','Summer','Spring']

if month == 12 or month <3:
    print(month_name[0])
elif month > 2 and month < 6:
    print(month_name[3])
elif month > 5 and month < 9:
    print(month_name[2])
else:
    print(month_name[1])

# Вариант через словарь
month = int(input('Введите число месяца: '))
month_dict = {1: 'Winter', 2:'Spring', 3:'Summer', 4:'Autumn'}

if month == 12 or month < 3:
    print(month_dict[1])
elif month > 2 and month < 6:
    print(month_dict[2])
elif month > 5 and month < 9:
    print(month_dict[3])
else:
    print(month_dict[4])
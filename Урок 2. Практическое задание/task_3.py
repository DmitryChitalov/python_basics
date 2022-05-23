"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

month = int(input("input num of month: "))
month_list = ['winter', 'spring', 'summer', 'autumn']
month_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer',
              9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
print(f'result through dict: {month_dict[month]}')
if 2 < month < 6:
    print(f'result through list: {month_list[1]}')
elif 5 < month < 9:
    print(f'result through list: {month_list[2]}')
elif 8 < month < 12:
    print(f'result through list: {month_list[3]}')
else:
    print(f'result through list: {month_list[0]}')

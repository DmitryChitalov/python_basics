"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

# dict ver

month = int(input('Введите месяц в виде целого числа от 1 до 12: '))

month_list = {1: 'winter', 2: 'winter', 12: 'winter',
              3: 'spring', 4: 'spring', 5: 'spring',
              6: 'summer', 7: 'summer', 8: 'summer',
              9: 'autumn', 10: 'autumn', 11: 'autumn'}

for key, value in month_list.items():
    if key == month:
        print(key, 'is', value)


# list ver

month = int(input('Введите месяц в виде целого числа от 1 до 12: '))

month_list = [None, 'Jan winter', 'Feb winter', 'March spring', 'Apr spring', 'May spring', 'June summer',
              'July summer',
              'Aug summer', 'Sep autumn', 'Oct autumn', 'Nov autumn', 'Dec winter']

for i in month_list:
    if month_list.index(i) == month:
        print(month_list.index(i), 'is', i)